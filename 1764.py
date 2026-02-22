import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, m = map(int, input().rstrip().split())
a = set()
b = set()
for _ in range(n):
    a.add(input().rstrip())

for _ in range(m):
    b.add(input().rstrip())

a = a & b
a = list(a)
a.sort()
print(len(a), *a, sep="\n")