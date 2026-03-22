import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, m = map(int, input().rstrip().split())
a = list(map(int, input().rstrip().split()))
s = [0] * n
s[0] = a[0]

cnt = [0] * m
for i in range(1, n):
    s[i] = s[i-1] + a[i]
    
for i in range(n):
    cnt[s[i] % m] += 1

result = cnt[0]
for i in range(m):
    result += math.comb(cnt[i], 2)

print(result)