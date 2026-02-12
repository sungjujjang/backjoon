import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input().rstrip())
print(int((n-2)*(n-1) * n/6))
print(3)