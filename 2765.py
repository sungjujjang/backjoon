import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
li = [list(input().strip()) for _ in range(n)]

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(sx, sy, visited):
    q = deque([(sx, sy)])
    visited[sx][sy] = True
    color = li[sx][sy]

    while q:
        x, y = q.popleft()

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy

            if (
                0 <= nx < n
                and 0 <= ny < n
                and not visited[nx][ny]
                and li[nx][ny] == color
            ):
                visited[nx][ny] = True
                q.append((nx, ny))


# 일반인
visited = [[False] * n for _ in range(n)]
normal = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, visited)
            normal += 1

# 적록색약 처리
for i in range(n):
    for j in range(n):
        if li[i][j] == 'R':
            li[i][j] = 'G'

visited = [[False] * n for _ in range(n)]
color_blind = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, visited)
            color_blind += 1

print(normal, color_blind)