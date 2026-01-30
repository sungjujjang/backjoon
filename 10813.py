import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())
bucket = [i for i in range(0, n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    temp = bucket[a]
    bucket[a] = bucket[b]
    bucket[b] = temp

del bucket[0]
print(*bucket)