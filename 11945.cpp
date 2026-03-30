#include <stdio.h>

int main() {
	int n, m;
	scanf("%d %d", &n, &m);
	char tmp[m];
	for (int i=0; i<n; i++) {
		scanf("%s", tmp);
		for (int j=m-1; j>=0; j--) {
			printf("%c", tmp[j]);
		}
		printf("\n");
	}
}
