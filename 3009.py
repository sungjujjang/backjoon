import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

xs = []
ys = []

for _ in range(3):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)

for x in xs:
    if xs.count(x) == 1:
        print(x, end=" ")
        
for y in ys:
    if ys.count(y) == 1:
        print(y, end=" ")