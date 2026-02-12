import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = 1000 - int(input())
moneys = [500, 100, 50, 10, 5, 1]
total = 0

for m in moneys:
    total += n//m
    n = n%m

print(total)