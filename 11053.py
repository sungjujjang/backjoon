import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input().rstrip())
a = list(map(int, input().rstrip().split()))
dp = [1] * (n+1)

for i in range(0, n):
    for j in range(0, i):
        if a[i] > a[j]:
            dp[i] = max(dp[j]+1, dp[i])

print(max(dp))