import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())
dp = [0, 0]

for i in range(2, n+1):
    tmp = dp[i - 1] + 1
    if i % 2 == 0:
        tmp = min(tmp, dp[i//2] + 1)
    if i % 3 == 0:
        tmp = min(tmp, dp[i//3] + 1)
    dp.append(tmp)

print(dp[n])