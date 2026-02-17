import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input().rstrip())
dungchi = []
for _ in range(n):
    dungchi.append(list(map(int, input().rstrip().split())))

for i in range(n):
    count = 1
    for j in range(n):
        if dungchi[i][0] < dungchi[j][0] and dungchi[i][1] < dungchi[j][1]:
            count += 1
    print(count, end=" ")