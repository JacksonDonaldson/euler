#include <stdio.h>
#include<math.h>
#include <stdlib.h>
#include <limits.h>
#include <float.h>
long largest = 0;
long int i;
long long num = 600851475143;
int done;
void main() {
	printf("%d\n", num);
	while (num != (long)1) {
		printf("\n%d", (num / (long)3));
		i = (long)1;
		done = 0;
		while (!done) {
			i += (long)1;
			if ((num % i) == 0) {
				num = num / i;
				if (i > largest) {
					largest = i;
				}
				done = 1;
			}
			
		}
		printf("\n%d", i);
	}
	printf("\n%d", largest);
}