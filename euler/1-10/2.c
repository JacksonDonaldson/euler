#include <stdio.h>
int total;
int num1 = 1;
int num2 = 2;
int stor;
int main() {
	while (num2 < 4000000) {
		if (num2 % 2 == 0) {
			total += num2;
		}
		stor = num2;
		num2 += num1;
		num1 = stor;
	}
	printf("%d ", total);
}