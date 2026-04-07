import sys
import math

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
a = [min(list(map(int, input().rstrip().split()))) for _ in range(n)]

# print(max(a))
print(a.index(max(a)))