#include <stdio.h>

int main() {
	int x_li[1001] = {0};
	int y_li[1001] = {0};
	int xs[3];
	int ys[3];
	int i, x, y;
	for (i = 0; i < 3; i++) {
		scanf("%d %d", &x, &y);
		xs[i] = x;
		ys[i] = y;
		x_li[x] += 1;
		y_li[y] += 1;
	}
	for (i = 0; i < 3; i++) {
		if (x_li[xs[i]] == 1) {
			x = xs[i];
		}
		if (y_li[ys[i]] == 1) {
			y = ys[i];
		}
	}
	printf("%d %d", x, y);
	return 0;
}
