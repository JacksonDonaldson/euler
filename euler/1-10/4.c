#include<stdio.h>
#include<math.h>
int largest = 0;
int pal(int n) {
	char* nStr;
	sprintf(nStr, "%d", n);
	int len = floor(log10(n)) + 1;
	int halflen = floor(len / 2);
	//printf("new");
	//printf("%d \n", nStr);
	//printf("%d \n", len);
	//printf("%d \n", halflen);
	int good = 1;
	for (int k = 0; k < halflen; k++) {
		if(nStr[k] != nStr[len - 1 - k]){
			good = 0;

		}
	}
	return good;
}

void main() {
	for (int i=1; i < 1000; i++) {
		for (int j=1; j < 1000; j++) {
			if(pal(i * j) == 1) {
				if (i * j > largest) {
					largest = i * j;
				}
			}
		}
	}
	printf("%d", largest);
}
