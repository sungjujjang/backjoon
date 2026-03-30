import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, m = map(int, input().rstrip().split())
for _ in range(n):
    print(*list(reversed(input().rstrip())), sep="")