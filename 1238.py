import sys
import math
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(1000000)
INF = float('inf')

def dxtra(graph, start):
    n = len(graph)
    
    len_ = [INF] * n
    len_[start] = 0
    
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        now_len, node = heapq.heappop(heap)

        if now_len > len_[node]:
            continue

        for next_node, weight in graph[node]:
            new_len = now_len + weight
            
            if new_len < len_[next_node]:
                len_[next_node] = new_len
                heapq.heappush(heap, (new_len, next_node))

    return len_

n, m, x = map(int, input().rstrip().split())
grap = [[] for i in range(n+1)]
reverse_grap = [[] for i in range(n+1)]
for _ in range(m):
    start, end, wg = map(int, input().rstrip().split())
    grap[start].append([end, wg])
    reverse_grap[end].append([start, wg])

xton = dxtra(reverse_grap, x)
ntox = dxtra(grap, x)
max_stu = float("-inf")

for i in range(1, n+1):
    total = xton[i]+ntox[i]
    max_stu = max(max_stu, total)
print(max_stu)