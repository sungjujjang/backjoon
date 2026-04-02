import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input().rstrip())
for i in range(n, 0, -1):
    print(" "*(n-i), end="")
    print("*"*i)