import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input().rstrip())
keys = []
for i in range(n):
    n, a, b, c = input().rstrip().split()
    keys.append([n, int(a), int(b), int(c)])

keys.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for name in keys:
    print(name[0])