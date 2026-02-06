import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input().rstrip())
arr = []

for i in range(n):
    arr.append(int(input().rstrip()))

arr.sort()
for i in arr:
    print(i)