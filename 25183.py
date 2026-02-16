import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input().rstrip())
lotto = list(map(ord, input().rstrip()))

stack = 1
for i in range(1, n):
    if lotto[i] == lotto[i-1] + 1 or lotto[i] == lotto[i-1] - 1:
        stack += 1
    else:
        stack = 1
    if stack == 5:
        print("YES")
        exit(0)
print("NO")
