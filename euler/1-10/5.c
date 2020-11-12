#include <stdio.h>
#include <time.h> 
#include <sys/time.h>
int num = 20;
int notdone = 1;
clock_t start, end;
struct timeval t1, t0;
void main() {
	start = clock();
	gettimeofday(&t0, 0);
	while (notdone) {
		num++;
		int good = 1;
		for (int i = 2; i <= 20; i++) {
			if (num % i != 0) {
				good = 0;
				break;
			}
		}
		if (good) {
			notdone = 0;
		}
	}
	gettimeofday(&t1, 0);
	long elapsed = ((t1.tv_sec - t0.tv_sec) * 1000000 + t1.tv_usec - t0.tv_usec);
	double test = elapsed /1000000;
	printf("%d", elapsed);
	printf("\n%d", test);
	printf("\n%d", num);
	end = clock();
	printf("%6.3f", end);
	printf("\n%f", start);
	printf("\n%f", (end - start));
}
