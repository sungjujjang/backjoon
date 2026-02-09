import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

a, b = map(int, input().split())
limit = int(math.sqrt(b))

sosu = [True] * (limit + 1)
sosu[0] = sosu[1] = False
sosulist = []

for i in range(2, int(math.sqrt(limit)) + 1):
    if sosu[i]:
        for j in range(i * i, limit + 1, i):
            sosu[j] = False

for i in range(2, limit + 1):
    if sosu[i]:
        sosulist.append(i)
# print(*sosulist)
count = 0
for sosu in sosulist:
    temp = sosu * sosu
    while temp <= b:
        if a <= temp:
            count += 1
        temp *= sosu

print(count)