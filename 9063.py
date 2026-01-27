import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

xmin = 10000
xmax = -10000
ymin = 10000
ymax = -10000

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    xmin = min(xmin, x)
    xmax = max(xmax, x)
    ymin = min(ymin, y)
    ymax = max(ymax, y)

print((xmax-xmin)*(ymax-ymin))