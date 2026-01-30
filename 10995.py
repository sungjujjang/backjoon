import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())
for i in range(0, n):
    for j in range(0, n*2):
        if (i+j) % 2 != 0:
            print(" ", end="")
        else:
            print("*", end="")
    print()