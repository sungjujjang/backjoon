import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

li = [0, 1, 1, 1]
t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    for i in range(len(li)-1, n+1):
        li.append(li[i-1] + li[i-2])
    print(li[n])