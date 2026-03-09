import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    nxt = n+1
    n %= 100
    if nxt % n:
        print("Bye")
    else:
        print("Good")