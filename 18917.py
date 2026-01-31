import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())

s = 0
xor = 0

for _ in range(n):
    q = list(map(int, input().split()))
    if q[0] == 1:
        s += q[1]
        xor = xor ^ q[1]
    elif q[0] == 2:
        s -= q[1]
        xor = xor ^ q[1]
    elif q[0] == 3:
        print(s)
    else:
        print(xor)