import sys
import math

input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
cnt = 0

while n > 1:
    if n%k == 0:
        cnt += 1
        n //= k
    else:
        cnt += 1
        n -= 1
        
print(cnt)

# dp[n] = n을 1로 만드는 경우의 수
dp = [0] * (n+1)
dp[2] = 1 # 2-1
dp[3] = 1 # 3//3

