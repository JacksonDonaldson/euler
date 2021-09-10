#include <stdio.h>
#include <math.h>
long goodMask; // 0xC840C04048404040 computed below



int isSquare(int x) {
	// This tests if the 6 least significant bits are right.
	// Moving the to be tested bit to the highest position saves us masking.
	if (goodMask << x >= 0) return 0;
	// Now x is either 0 or odd.
	// In binary each odd square ends with 001.
	// Postpone the sign test until now; handle zero in the branch.
	if ((x & 7) != 1 | x <= 0) return x == 0;
	// Do it in the classical way.
	// The correctness is not trivial as the conversion from long to double is lossy!
	int tst = (int)sqrt(x);
	if (tst * tst == x) {
		return 1;
	}
	return 0;
}

int findX(int d) {
	int x = 1;
	int add = 3;
	while(true){
		x += add;
		add+=2
		if (isSquare((x -1)/d) == 1:
			return Math.sqrt(x);
}
	}
}
int main() {
	for (int i = 0; i < 64; ++i) goodMask |= Long.MIN_VALUE >> > (i*i);
	int max
	for (int d = 2; d < 1001; d++) {
		value = findX(d);
		if (value > max) {
			max = value;
			printf("Max: %d", max);
		}
	}
	return 0;
}