import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input().rstrip())
keys = []
for i in range(n):
    keys.append(input().rstrip())

keys = list(set(keys))
keys.sort(key=lambda x: (len(x), x))
print(*keys, sep="\n")