import sys
import math

input = sys.stdin.readline

m, n = map(int, input().split())

sosu = [True] * (n + 1)
sosu[0] = sosu[1] = False

for i in range(2, int(math.sqrt(n)) + 1):
    if sosu[i]:
        for j in range(i * i, n + 1, i):
            sosu[j] = False

for i in range(m, n + 1):
    if sosu[i]:
        print(i)