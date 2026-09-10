#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#define NUMBERS 20
#define DIGITS 3
#define BASE 10

int nums[NUMBERS];

typedef struct {
    int *values;
    int size;
} Bucket;

Bucket buckets[BASE];

int main(void) {

    srand(time(NULL));

    for (int i = 0; i < NUMBERS; i++) {
        nums[i] = rand() % 1000;
    }

    for (int i = 0; i < BASE; i++) {
        buckets[i].values = malloc(NUMBERS * sizeof(int));
        buckets[i].size = 0;
    }


    int divisor = 1;

    for (int d = 1; d <= DIGITS; d++) {

        for (int i = 0; i < NUMBERS; i++) {
            int tray = (nums[i] / divisor) % 10;
            buckets[tray].values[buckets[tray].size] = nums[i];
            buckets[tray].size++;
        }

        int n=0;
        int m=0;
        for (int i = 0; i < NUMBERS; i++) {
            if (m < buckets[n].size) {
                nums[i] = buckets[n].values[m];
                m++;
            } else {
                m = 0;
                n++;
                i--;
            }
        }

        for (int i = 0; i < NUMBERS; i++) {
            buckets[i].size = 0;
        }

        divisor *= 10;
    
    }


    for (int i = 0; i < NUMBERS; i++) {
        printf("%d\n", nums[i]);
    }
    

    return 0;
}