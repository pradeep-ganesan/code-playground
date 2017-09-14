#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <assert.h>

#define RINGSZ 10

struct ringbuf {
    int ring[RINGSZ];
    int tip, tail;
    int ringfull, ringempty;
    pthread_mutex_t *mut;
    pthread_cond_t *condnotfull;
    pthread_cond_t *condnotempty;
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
    pthread_create(&prodth, NULL, producer, (void *)ring);
    pthread_create(&conth, NULL, consumer, (void *)ring);

    pthread_join(prodth, NULL);
    pthread_join(conth, NULL);

    pthread_mutex_destroy(ring->mut);
    free(ring->mut);
    pthread_cond_destroy(ring->condnotfull);
    free(ring->condnotfull);
    pthread_cond_destroy(ring->condnotempty);
    free(ring->condnotempty);
    free(ring);

    return 0;
}

struct ringbuf *initring() {
    struct ringbuf *r = (struct ringbuf *) malloc(sizeof(struct ringbuf));
    r->tip = 0;
    r->tail = 0;
    r->ringfull = 0;
    r->ringempty = 1;
    r->mut = (pthread_mutex_t *) malloc(sizeof(pthread_mutex_t));
    assert(r->mut);
    r->condnotfull = (pthread_cond_t *)malloc(sizeof(pthread_cond_t));
    assert(r->condnotfull);
    r->condnotempty = (pthread_cond_t *)malloc(sizeof(pthread_cond_t));
    assert(r->condnotempty);

    pthread_mutex_init(r->mut, NULL);
    pthread_cond_init(r->condnotfull, NULL);
    pthread_cond_init(r->condnotempty, NULL);

    return r;
}

void *producer(void *r) {
    struct ringbuf *ring = (struct ringbuf *) r;
    for(int i=0; i<20; i++) {
        assert(ring->mut);
        pthread_mutex_lock(ring->mut);
        while (ring->ringfull) {
            printf("waiting on full ring\n");
            pthread_cond_wait(ring->condnotfull, ring->mut);
        }
        ringadd(ring, i);
        pthread_mutex_unlock(ring->mut);
        pthread_cond_signal(ring->condnotempty);
    }

    return NULL;
}

void *consumer(void *r) {
    int n;
    struct ringbuf *ring = (struct ringbuf *) r;
    for(int i=0; i<20; i++) {
        assert(ring->mut);
        pthread_mutex_lock(ring->mut);
        while (ring->ringempty) {
            printf("waiting on empty ring\n");
            pthread_cond_wait(ring->condnotempty, ring->mut);
        }
        ringremove(ring, &n);
        pthread_mutex_unlock(ring->mut);
        pthread_cond_signal(ring->condnotfull);
    }    

    return NULL;
}

void ringadd(struct ringbuf *r, int n) {
    r->ring[r->tip++] = n;
    printf("added item: %d\n", n);
    if (r->tip == RINGSZ)
    {
        r->tip = 0;
    }
    if (r->tip == r->tail) {
        printf("ring is now full\n");
        r->ringfull = 1;
    }
    r->ringempty = 0;
}

void ringremove(struct ringbuf *r, int *n) {
    *n = r->ring[r->tail++];
    printf("removed item: %d\n", *n);
    if (r->tail == RINGSZ)
        r->tail = 0;
    if (r->tail == r->tip) {
        printf("ring is now empty\n");
        r->ringempty = 1;
    }
    r->ringfull = 0;
}