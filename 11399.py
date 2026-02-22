import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input().rstrip())
p = list(map(int, input().rstrip().split()))
for i in range(n):
    p[i] = (i+1, p[i])

p.sort(key=lambda x: x[1])
total = 0
temp = 0
for i in range(n):
    temp += p[i][1]
    total += temp

print(total)