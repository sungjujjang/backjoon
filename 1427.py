import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

counts = [0] * 10
n = list(input().rstrip())
for s in n:
    counts[int(s)] += 1

for i in range(9, -1, -1):
    print(str(i)*counts[i], end="")