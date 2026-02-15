import sys
import math
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

m, n, h = map(int, input().rstrip().split())
tomato = [[[0] * (m+1) for _ in range(n+1)] for __ in range(h+1)]
quque = deque()
ck_list = set()
for _h in range(1, h+1):
    for _n in range(1, n+1):
        line = list(map(int, input().rstrip().split()))
        for _m in range(1, m+1):
            ck_list.add(line[_m-1])
            if line[_m-1] == 1:
                quque.append([_h, _n, _m])
            tomato[_h][_n][_m] = line[_m-1]

if ck_list == {1, -1} or ck_list == {1}:
    print(0)
    exit()

def check(_h, _n, _m):
    if _h > h or _h < 1:
        return False
    if _n > n or _n < 1:
        return False
    if _m > m or _m < 1:
        return False
    if tomato[_h][_n][_m] != 0:
        return False
    return True

dirs = [
    [1, 0, 0],
    [-1, 0, 0],
    [0, 1, 0],
    [0, -1, 0],
    [0, 0, 1],
    [0, 0, -1]
]
# print(quque)
while quque:
    temp = quque.popleft()
    # print(temp)
    days = tomato[temp[0]][temp[1]][temp[2]]
    for d in dirs:
        _h, _n, _m = temp[0]+d[0], temp[1]+d[1], temp[2]+d[2]
        if check(_h, _n, _m):
            tomato[_h][_n][_m] = days+1
            quque.append([_h, _n, _m])

result = -1
is_all = False
for _h in range(1, h+1):
    for _n in range(1, n+1):
        for _m in range(1, m+1):
            now = tomato[_h][_n][_m]
            if now == 0:
                print(-1)
                exit(0)
            result = max(now, result)

result -= 1
print(result)