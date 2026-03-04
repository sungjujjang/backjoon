import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input().rstrip())
for i in range(1, n+1):
    print(" "*(n-i)+"*"*(1+2*(i-1)))
for i in range(n-1, 0, -1):
    print(" "*(n-i)+"*"*(1+2*(i-1)))