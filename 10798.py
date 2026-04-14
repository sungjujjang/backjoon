import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

chars = []
lenner = []

for _ in range(5):
    l = list(input().rstrip())
    chars.append(l)
    lenner.append(len(l))

for i in range(max(lenner)):
    for j in range(5):
        if lenner[j] >= i+1:
            print(chars[j][i], end="")