import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

t = int(input().rstrip())
a, b, c = 300, 60, 10

a1 = t // a
t %= a
b1 = t // b
t %= b
c1 = t // c
t %= c

if t != 0:
    print(-1)
else:
    print(a1, b1, c1)