import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

a.sort()
for i in a:
    print(i)