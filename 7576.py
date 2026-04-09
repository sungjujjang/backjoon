import sys
import math
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

m, n = map(int, input().rstrip().split())
tomato = [[0] * (m+1) for _ in range(n+1)]
quque = deque()
ck_list = set()
for _n in range(1, n+1):
    line = list(map(int, input().rstrip().split()))
    for _m in range(1, m+1):
        ck_list.add(line[_m-1])
        if line[_m-1] == 1:
            quque.append([_n, _m])
        tomato[_n][_m] = line[_m-1]

if ck_list == {1, -1} or ck_list == {1}:
    print(0)
    exit()

def check(_n, _m):
    if _n > n or _n < 1:
        return False
    if _m > m or _m < 1:
        return False
    if tomato[_n][_m] != 0:
        return False
    return True

dirs = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0]
]
# print(quque)
while quque:
    temp = quque.popleft()
    # print(temp)
    days = tomato[temp[0]][temp[1]]
    for d in dirs:
        _n, _m = temp[0]+d[0], temp[1]+d[1]
        if check(_n, _m):
            tomato[_n][_m] = days+1
            quque.append([_n, _m])

result = -1
is_all = False
for _n in range(1, n+1):
    for _m in range(1, m+1):
        now = tomato[_n][_m]
        if now == 0:
            print(-1)
            exit(0)
        result = max(now, result)

result -= 1
print(result)