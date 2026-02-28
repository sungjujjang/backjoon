import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input().rstrip())
if n % 2 == 0:
    print((n // 2 + 1) ** 2)
else:
    print((n // 2 + 1) * (n // 2 + 2))