#include <stdio.h>

void newab(int* num) {
	*num = *num / 2 + *num % 2;
} //  포인터 사용해서 리턴 없이 메모리 직접 참조 -> void

int ab(int num) {
	num = num / 2 + num % 2;
	return num;
} //  포인터 사용해서 리턴 없이 메모리 직접 참조 -> void

int main() {
	int n, a, b;
	scanf("%d %d %d", &n, &a, &b);
	n = 0;
	while (a != b) {
		n++;
		newab(&a);
		newab(&b);
	}
// newab();
	
//	while (a != b) {
//		n++;
//		a = ab(a);
//		b = ab(b);
//	}
// ab();
	printf("%d", n);
}
