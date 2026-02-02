import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

StokuList = [list(map(int, input().strip())) for _ in range(9)]

BlankList = []
for y in range(9):
    for x in range(9):
        if StokuList[y][x] == 0:
            BlankList.append((y, x))

def Stoku(idx):
    if len(BlankList) <= idx:
        for row in StokuList:
            print(''.join(map(str, row)))
        sys.exit()

    y, x = BlankList[idx]

    used = set()
    for i in range(9):
        used.add(StokuList[y][i])
        used.add(StokuList[i][x])

    sy = (y // 3) * 3
    sx = (x // 3) * 3
    for i in range(sy, sy + 3):
        for j in range(sx, sx + 3):
            used.add(StokuList[i][j])

    values = [v for v in range(1, 10) if v not in used]

    for value in values:
        StokuList[y][x] = value
        Stoku(idx + 1)
        StokuList[y][x] = 0

Stoku(0)