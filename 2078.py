import sys
import math

input = sys.stdin.readline
# sys.setrecursionlimit(1000000)

l = 0
r = 0
a, b = map(int, input().rstrip().split())

while a>1 and b>1:
    if a > b:
        l += a//b
        a %= b
    elif a < b:
        r += b//a
        b %= a

l += a-1
r += b-1
print(l, r)