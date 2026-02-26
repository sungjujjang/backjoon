import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input().rstrip())
table = [[0] * (n+1)]
dp = [[-1] * (n+1) for _ in range(n+1)]

for i in range(n):
    line = [0] + list(map(int, input().rstrip().split()))
    table.append(line)

dp[1][1] = table[1][1]
max_m = -1

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j == 1:
            continue
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) * 2 + table[i][j]
        max_m = max(max_m, dp[i][j])

print(max_m)