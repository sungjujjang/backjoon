import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)
world = set()
sum_ = 0

n, m = map(int, input().rstrip().split())
for i in range(n):
    world.add(input().rstrip())
for i in range(m):
    if input().rstrip() in world:
        sum_ += 1

print(sum_)