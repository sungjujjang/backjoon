import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input().rstrip())
a = list(map(int, input().rstrip().split()))
dp_front = [1] * (n)
dp_back = [1] * (n)

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp_front[i] = max(dp_front[i], dp_front[j] + 1)

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if a[i] > a[j]:
            dp_back[i] = max(dp_back[i], dp_back[j] + 1)
            
dp = [(dp_front[i] + dp_back[i] - 1) for i in range(0, n)]
print(max(dp))