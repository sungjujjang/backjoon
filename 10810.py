import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n,m = map(int, input().split())
bucket = [0] * (n+1)
for _ in range(m):
    i, j, k = map(int, input().split())
    for b in range(i, j+1):
        bucket[b] = k

del bucket[0]
print(*bucket)