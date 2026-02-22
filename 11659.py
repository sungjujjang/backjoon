import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, m = map(int, input().rstrip().split())
a = list(map(int, input().rstrip().split()))
s = [0]
temp = 0
for i in a:
    temp += i
    s.append(temp)

for _ in range(m):
    i, j = map(int, input().rstrip().split())
    print(s[j] - s[i-1])