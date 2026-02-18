import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input().rstrip())
xys = []
for i in range(n):
    xys.append(list(map(int, input().rstrip().split())))

xys.sort(key=lambda x: (x[1], x[0]))
for x, y in xys:
    print(x, y)