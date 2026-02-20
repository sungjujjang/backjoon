import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input().rstrip())

if n == 1:
    print(1)
    exit(0)

dp = [0] * (n+1)
dp[0] = 1
dp[1] = 1
dp[2] = 3

for i in range(3, n+1):
    dp[i] = 2 * dp[i-2] + dp[i-1]

result = (dp[n] + dp[n//2] + dp[n//2 - 1] * 2 * abs(n % 2 - 1)) // 2
print(result)