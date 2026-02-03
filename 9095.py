import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

dp = [0, 1, 2, 4]
mt = 3

t = int(input())
for _ in range(t):
    n = int(input())
    if mt >= n:
        print(dp[n])
    else:
        for i in range(mt+1, n+1):
            dp.append(dp[i-1] + dp[i-2] + dp[i-3])
        mt = n
        print(dp[n])