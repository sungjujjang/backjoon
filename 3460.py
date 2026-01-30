import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

t = int(input())
for _ in range(t):
    n = int(input())
    i = 0
    while n > 0:
        if n % 2 == 1:
            print(i, end=" ")
        n //= 2
        i += 1