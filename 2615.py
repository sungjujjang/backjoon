import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

omok = []
for i in range(19):
    omok.append(list(map(int, input().split())))

dircheck = [[0, 1], [1, 0], [1, 1], [1, -1]]
ansdir = [0, 0]
ans = 0

for y in range(19):
    for x in range(19):
        if omok[y][x] != 0:
            ans = omok[y][x]
            ansdir = [x, y]
            for dx, dy in dircheck:
                tx, ty = x, y
                strick = 1
                py = y - dy
                px = x - dx
                if 0 <= py < 19 and 0 <= px < 19:
                    if omok[py][px] == ans:
                        continue
                for i in range(4):
                    tx += dx
                    ty += dy
                    if tx < 0 or ty < 0:
                        break
                    if tx > 18 or ty > 18:
                        break
                    if omok[ty][tx] == ans:
                        strick += 1
                    else:
                        break
                if strick == 5:
                    ny = ty + dy
                    nx = tx + dx
                    if 0 <= ny < 19 and 0 <= nx < 19:
                        if omok[ny][nx] == ans:
                            continue
                    print(ans)
                    print(ansdir[1] + 1, ansdir[0] + 1)
                    exit()
print(0)