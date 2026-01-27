import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())
li = list(map(int, input().split()))
v = int(input())

cnt = 0
for i in range(0, n):
    if li[i] == v: cnt += 1
print(cnt)