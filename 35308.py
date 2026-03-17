import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

for _ in range(int(input().rstrip())):
    n, k = map(int, input().rstrip().split())

    if n == 1 and k == 1:
        print(1)
    elif k == 2:
        for i in range(2, n+1):
            print(i, end=" ")
        print(1)
    else:
        print(-1)