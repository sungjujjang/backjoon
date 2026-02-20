import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input().rstrip())

if n % 2 == 1:
    print(0)
    exit(0)

dp = [0] * (n+1)
dp[0] = 1
dp[2] = 3

for i in range(4, n+1, 2):
    dp[i] = dp[i-2] * 4 + dp[i-4] * -1
print(dp[n])