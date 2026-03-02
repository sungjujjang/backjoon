import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input().rstrip())
first = []
second = []

for _ in range(n):
    first.append(list(map(int, input().rstrip().split())))
for _ in range(n):
    second.append(list(map(int, input().rstrip().split())))
first.sort()
second.sort()

print(second[0][0] - first[0][0],  second[0][1] - first[0][1])