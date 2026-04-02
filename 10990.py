import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input().rstrip())
print(" "*(n-1) + "*")
for i in range(2, n+1):
    print(" "*(n-i) + "*" + " "*(i*2-3) + "*")