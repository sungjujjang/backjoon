import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(100000000)

def check(n, m, x, y):
    n -= 1
    m -= 1
    if x < 0 or y < 0:
        return False
    if x > m or y > n:
        return False
    return True

def dfs(x, y):
    global visited, m, n
    if visited[x][y] == 1:
        visited[x][y] = 0
        dirc = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        for dx, dy in dirc:
            if check(n, m, x + dx, y + dy):
                dfs(x + dx, y + dy)

t = int(input())
for tst in range(t):
    cnt = 0
    m, n, k = map(int, input().split())
    visited = [[0] * n for v in range(m)]
    for _ in range(k):
        x, y = map(int, input().split())
        visited[x][y] = 1
    for x in range(m):
        for y in range(n):
            if visited[x][y] == 1:
                dfs(x, y)
                cnt += 1
    print(cnt)
    