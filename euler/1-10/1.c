#include <stdio.h>
int main() {
	int total = 0;
	for (int i = 0; i < 1000; i++) {
		if (i % 3 == 0) {
			total += i;
		}
		else if (i % 5 == 0) {
			total += i;
		}
	}
	printf("%d ",total);
	return 0;
}