#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <assert.h>
#include <unistd.h>

#define RINGSZ 1000
#define LOOP 20

struct ringbuf {
    int ring[RINGSZ];
    int tip, tail;
    int ringfull, ringempty;
    int readcount;
    int reading, writing;
    pthread_mutex_t *resourcelock;
    pthread_mutex_t *readaccess;
    pthread_cond_t *cond;
    pthread_cond_t *allowread;
    pthread_cond_t *allowwrite;
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
    assert(ring->resourcelock);

    printf("rings created\n");
    pthread_create(&prodth, NULL, producer, (void *)ring);
    pthread_create(&conth, NULL, consumer, (void *)ring);

    printf("threads created\n");
    pthread_join(prodth, NULL);
    pthread_join(conth, NULL);

    pthread_mutex_destroy(ring->resourcelock);
    pthread_mutex_destroy(ring->readaccess);
    free(ring->resourcelock);
    free(ring->readaccess);
    pthread_cond_destroy(ring->cond);
    free(ring->cond);
    free(ring);
    return 0;
}

struct ringbuf *initring() {
    struct ringbuf *r = (struct ringbuf *) malloc(sizeof(struct ringbuf));
    r->tip = 0;
    r->tail = 0;
    r->reading = 0;
    r->writing = 0;
    r->readcount = 0;
    r->ringfull = 0;
    r->ringempty = 1;
    r->resourcelock = (pthread_mutex_t *) malloc(sizeof(pthread_mutex_t));
    assert(r->resourcelock);
    r->readaccess = (pthread_mutex_t *) malloc(sizeof(pthread_mutex_t));
    assert(r->readaccess);
    r->cond = (pthread_cond_t *) malloc(sizeof(pthread_cond_t));
    assert(r->cond);
    //r->allowread = (pthread_cond_t *) malloc(sizeof(pthread_cond_t));
    //r->allowwrite = (pthread_cond_t *) malloc(sizeof(pthread_cond_t));

    pthread_mutex_init(r->resourcelock, NULL);
    pthread_mutex_init(r->readaccess, NULL);

    pthread_cond_init(r->cond, NULL);
    //pthread_cond_init(r->allowread, NULL);
    //pthread_cond_init(r->allowwrite, NULL);

    return r;
}

//reader
void *consumer(void *r) {
    printf("in reader\n");
    int n;
    struct ringbuf *ring = (struct ringbuf *) r;
    for(int i=0; i<LOOP; i++) {
        //entry section
        printf("acquiring access lock in reader\n");
        assert(ring->readaccess);
        pthread_mutex_lock(ring->readaccess);
        ring->readcount++;
        printf("obtained access lock in reader\n");
        if (ring->readcount == 1) {
            printf("acquiring resource lock in reader\n");
            pthread_mutex_lock(ring->resourcelock);
            while (ring->writing) {
                printf("waiting on resource lock in reader\n");
                pthread_cond_wait(ring->cond, ring->resourcelock);
            }
            printf("obtained resource lock in reader\n");
        }
        pthread_mutex_unlock(ring->readaccess);

        //critical section
        ringremove(ring, &n);
        printf("read item %d\n", n);

        //exit section
        pthread_mutex_lock(ring->readaccess);
        ring->readcount--;
        if (ring->readcount == 0) {
            pthread_mutex_unlock(ring->resourcelock);
            pthread_cond_signal(ring->cond);
        }
        pthread_mutex_unlock(ring->readaccess);
        usleep(2);
    }
    printf("reader done\n");

    return NULL;
}

// writer
void *producer(void *r) {
    printf("in writer\n");
    struct ringbuf *ring = (struct ringbuf *) r;
    for(int i=0; i<LOOP; i++) {
        //entry section
        printf("acquiring resource lock in writer\n");
        assert(ring->resourcelock);
        pthread_mutex_lock(ring->resourcelock);
        printf("obtained resource lock in writer\n");
        while (ring->readcount > 0) {
            printf("waiting on resource lock in writer\n");
            pthread_cond_wait(ring->cond, ring->resourcelock);
        }
        printf("obtained resource lock in writer\n");
        //critical section
        ring->writing = 1;
        ringadd(ring, i);
        //exit section
        ring->writing = 0;
        pthread_mutex_unlock(ring->resourcelock);
        pthread_cond_signal(ring->cond);
        usleep(2);
    }
    printf("writer done\n");

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