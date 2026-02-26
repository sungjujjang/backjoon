import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

max_num = 0
x, y = 0, 0

for i in range(9):
    line = list(map(int, input().rstrip().split()))
    for j in range(9):
        if line[j] > max_num:
            max_num = line[j]
            x, y = i+1, j+1

print(max_num)
print(x, y)