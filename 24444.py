import sys
import math
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, m, r = map(int, input().split())
visited = [False] * (n+1)
sunseo = [0] * (n+1)
ese = [[] for i in range(n+1)]

for ms in range(m):
    a, b = map(int, input().split())
    ese[a].append(b)
    ese[b].append(a)

for i in range(1, n+1):
    ese[i].sort()

queue = deque([r])

count = 1
while queue:
    c = queue.popleft()
    sunseo[c] = count
    count += 1
    visited[c] = True
    for v in ese[c]:
        if not visited[v]:
            visited[v] = True
            queue.append(v)

del sunseo[0]
print(*sunseo, sep="\n")