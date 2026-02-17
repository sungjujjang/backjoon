import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

up = [0] * 10000001
under = [0] * 10000001 # 0 포함

n = int(input().rstrip())
a = list(map(int, input().rstrip().split()))

m = int(input().rstrip())
ma = list(map(int, input().rstrip().split()))

for i in a:
    if i > 0:
        up[i] += 1
    else:
        under[i] += 1

for i in ma:
    if i > 0:
        print(up[i], end=" ")
    else:
        print(under[i], end=" ")