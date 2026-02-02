import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

a, b, c = map(int, input().split())
a, b, c = sorted([a, b, c])
if a+b > c:
    print(a+b+c)
else:
    print((a+b+c) - ((c-(a+b))+1))