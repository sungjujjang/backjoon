import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

while True:
    r, c = map(int, input().rstrip().split())
    if r == c == 0:
        break
    zirae = []
    for i in range(r):
        zirae.append(list(input().rstrip()))

    mr, mc = r-1, c-1

    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]

    for i in range(r):
        for j in range(c):
            if not zirae[i][j] == "*":
                count = 0
                for di, dj in dirs:
                    tmi, tmj = i+di, j+dj
                    if not 0 <= tmi <= mr:
                        continue
                    if not 0 <= tmj <= mc:
                        continue
                    if zirae[tmi][tmj] == "*":
                        count += 1
                zirae[i][j] = count
            print(zirae[i][j], end="")
        print()