import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

t = int(input())
moneys = [25, 10, 5, 1]
for _ in range(t):
    n = int(input())
    for m in moneys:
        print(n//m, end=" ")
        n %= m
    print()