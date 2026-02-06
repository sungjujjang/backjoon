import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

a, b = map(lambda n: int(n[::-1]), input().rstrip().split())
print(max(a, b))