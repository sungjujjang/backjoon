import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if (x1, y1) == (x2, y2):
        if r1 == r2:
            print(-1)
            continue
        else:
            print(0)
            continue
    distance = math.dist((x1, y1), (x2, y2))
    s = r1 + r2
    m = abs(r1 - r2)
    if distance > s:
        print(0)
    elif distance == s:
        print(1)
    elif distance < m:
        print(0)
    elif distance == m:
        print(1)
    else:
        print(2)
