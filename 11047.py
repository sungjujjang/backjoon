import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, k = map(int, input().rstrip().split())
coins = []
for _ in range(n):
    coins.append(int(input().rstrip()))

count = 0
for i in range(n-1, -1, -1):
    count += k // coins[i]
    k %= coins[i]
    if k == 0:
        break

print(count)