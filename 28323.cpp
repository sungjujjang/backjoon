# include <stdio.h>

int main() {
	int n, i, tmp, len;
	scanf("%d", &n);
	int a[n];
	for (i=0; i<n; i++) {
		scanf("%d", &a[i]);
	}
	tmp = 0;
	len = 1;
	for (i=1; i<n; i++) {
		if ((a[tmp]+a[i]) % 2 == 1) {
			len++;
			tmp = i;
		}
	}
	printf("%d", len);
}
