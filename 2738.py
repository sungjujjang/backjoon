import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())

a1 = [list(map(int, input().split())) for _ in range(n)]
a2 = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        print(a1[i][j] + a2[i][j], end=' ')
    print()