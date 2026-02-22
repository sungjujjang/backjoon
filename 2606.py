import sys
import math
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input().rstrip())
m = int(input().rstrip())
gan_line = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    gan_line[a].append(b)
    gan_line[b].append(a)

quque = deque([1])
visited[1] = True
count = 0
while quque:
    temp = quque.popleft()
    for i in gan_line[temp]:
        if visited[i]:
            continue
        visited[i] = True
        count += 1
        quque.append(i)

print(count)