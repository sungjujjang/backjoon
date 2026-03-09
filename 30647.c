#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct DATA {
	char name[20];
	int score;
	int isHidden;
} DATA;

int compare(const void* va, const void* vb) {
	DATA* a = (DATA*) va;
	DATA* b = (DATA*) vb;
	int result = b->score - a->score;
	if (result == 0) {
		result = strcmp(a->name, b->name);
	}
	return result;
}

int checktrue(char ch) {
	char a[3] = {',', '[', ']'};
	int i_;
	for (i_=0; i_<3; i_++) {
		if (ch == a[i_]) {
			return 0;
		}
	}
	return 1;
}

int main() {
	int n, i, j, tmpint;
	scanf("%d", &n);
	char *strings[n];
	int strings_len[n];
	char tmp[9999], tmp2[9999];
	DATA data[n];
	for (i=0; i<n; i++) {
		scanf("%s", tmp);
		strings_len[i] = strlen(tmp)+1;
		tmpint = 0;
		for (j=0; j<strings_len[i]; j++) {
			if (checktrue(tmp[j]) == 1) {
				tmp2[tmpint] = tmp[j];
				tmpint++;
			}
		}
		strings_len[i] = tmpint;
		strings[i] = (char*)malloc(strings_len[i]);
		strcpy(strings[i], tmp2);
//		printf("%s\n", strings[i]);
	}

	for (i=0; i<n; i++) {
		sscanf(strings[i], "{\"name\":\"%[^\"]\"\"score\":%d\"isHidden\":%d}", data[i].name, &data[i].score, &data[i].isHidden);
	}
	qsort(data, n, sizeof(DATA), compare);
	int rank = 1;
	for (i=0; i<n; i++) {
		if (i == 0 || data[i].score != data[i-1].score) {
			rank = i + 1;
		}
		if (data[i].isHidden == 0) {
			printf("%d %s %d\n", rank, data[i].name, data[i].score);	
		}
	}
	return 0;
}
