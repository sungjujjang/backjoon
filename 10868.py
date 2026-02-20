import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

a = []
n, m = map(int, input().rstrip().split())
log = int(math.log2(n)) + 1

for i in range(n):
    a.append(int(input().rstrip()))

dp = [[0]*log for _ in range(n)]

for i in range(n):
    dp[i][0] = a[i]

# 1<<j = 2^j, a << b = a * 2^b
def gae(n):
    return 1<<n

for j in range(1, log):
    for i in range(n - gae(j) + 1):
        dp[i][j] = min(
            dp[i][j-1],
            dp[i + gae(j-1)][j-1]
        )

for _ in range(m):
    a, b = map(int, input().rstrip().split())
    a -= 1
    b -= 1
    length = b-a + 1
    k = math.floor(math.log2(length))
    print(min(dp[a][k], dp[b-gae(k)+1][k]))