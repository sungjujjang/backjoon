import sys
import math
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, m, v = map(int, input().split())
manyvs = [[] for _ in range(0, n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    manyvs[a].append(b)
    manyvs[b].append(a)

for i in range(1, n+1):
    manyvs[i].sort()

visited = [False] * (n+1)
stack = deque([v])

while stack:
    cur = stack.pop()
    if visited[cur]:
        continue
    print(cur, end=" ")
    visited[cur] = True
    for c in reversed(manyvs[cur]):
        if visited[c] == False:
            stack.append(c)

print()

visited = [False] * (n+1)
quque = deque([v])
visited[v] = True

while quque:
    cur = quque.popleft()
    print(cur, end=" ")
    for c in manyvs[cur]:
        if visited[c] == False:
            quque.append(c)
            visited[c] = True