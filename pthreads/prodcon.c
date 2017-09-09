#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define RINGSZ 10

struct ringbuf {
    int ring[RINGSZ];
    int tip, tail;
    int ringfull, ringempty;
    pthread_mutex_t *mut;
    pthread_cond_t *cond;
};

struct ringbuf *initring();
void *producer(void *r);
void *consumer(void *r);
void ringadd(struct ringbuf *r, int n);
void ringremove(struct ringbuf *r, int *n);

int main()
{
    pthread_t prodth, conth;
    struct ringbuf *ring;

    ring = initring();
    pthread_create(&prodth, NULL, producer, (void *)&ring);
    pthread_create(&conth, NULL, consumer, (void *)&ring);

    pthread_join(prodth, NULL);
    pthread_join(conth, NULL);

    pthread_mutex_destroy(ring->mut);
    free(ring->mut);
    pthread_cond_destroy(ring->cond);
    free(ring->cond);

    return 0;
}

struct ringbuf *initring() {
    struct ringbuf *r = (struct ringbuf *) malloc(sizeof(struct ringbuf));
    r->tip = 0;
    r->tail = 0;
    r->ringfull = 0;
    r->ringempty = 1;
    r->mut = (pthread_mutex_t *) malloc(sizeof(pthread_mutex_t));
    r->cond = (pthread_cond_t *) malloc(sizeof(pthread_cond_t));

    pthread_mutex_init(r->mut, NULL);
    pthread_cond_init(r->cond, NULL);

    return r;
}

void *producer(void *r) {
    struct ringbuf *ring = (struct ringbuf *) r;
    for(int i=0; i<20; i++) {
        pthread_mutex_lock(ring->mut);
        while (ring->ringfull) {
            pthread_cond_wait(ring->cond, ring->mut);
        }
        ringadd(ring, i);
        pthread_mutex_unlock(ring->mut);
        pthread_cond_signal(ring->cond);
    }

    return NULL;
}

void *consumer(void *r) {
    int n;
    struct ringbuf *ring = (struct ringbuf *) r;
    for(int i=0; i<20; i++) {
        pthread_mutex_lock(ring->mut);
        while (ring->ringempty) {
            pthread_cond_wait(ring->cond, ring->mut);
        }
        ringremove(ring, &n);
        pthread_mutex_unlock(ring->mut);
        pthread_cond_signal(ring->cond);
    }    

    return NULL;
}

void ringadd(struct ringbuf *r, int n) {
    if (r->tip == RINGSZ) {
        r->tip = 0;
    }
    r->ring[r->tip++] = n;
    printf("added item: %d\n", n);
    if (r->tip == r->tail)
        r->ringfull = 1;
    r->ringempty = 0;
}

void ringremove(struct ringbuf *r, int *n) {
    if (r->tail == RINGSZ)
        r->tail = 0;
    *n = r->ring[r->tail++];
    if (r->tail == r->tip)
        r->ringempty = 1;
    r->ringfull = 0;
}