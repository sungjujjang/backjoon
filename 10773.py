import sys
from collections import deque
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

k = int(input())
stack = deque()

for _ in range(k):
    n = int(input())
    if n == 0:
        if stack:
            stack.pop()
    else:
        stack.append(n)

print(sum(stack))