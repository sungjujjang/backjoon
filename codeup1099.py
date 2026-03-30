import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

gami = []
for i in range(10):
    gami.append(list(map(int, input().rstrip().split())))

nowx, nowy = 1, 1
gami[nowy][nowx] = 9
while True:
    if nowx == 8 and nowy == 8:
        break
    if gami[nowy][nowx+1] == 1:
        nowy += 1
    elif gami[nowy+1][nowx] == 1 and gami[nowy][nowx+1] == 1:
        break
    else:
        nowx += 1
    if gami[nowy][nowx] == 2:
        gami[nowy][nowx] = 9
        break
    gami[nowy][nowx] = 9

for y in gami:
    print(*y, sep=" ")