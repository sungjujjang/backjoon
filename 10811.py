import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())
buckets = [0] + [i for i in range(1, n+1)]

for i in range(m):
    a, b = map(int, input().split())
    tmp = buckets[a:b+1]
    tmp.reverse()
    for j in range(a, b+1):
        buckets[j] = tmp[j-a]

del buckets[0]
print(*buckets)