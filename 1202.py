import sys
import math
import heapq
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, k = map(int, input().rstrip().split())
stars = [list(map(int, input().rstrip().split())) for _ in range(n)]
bags = [int(input().rstrip()) for _ in range(k)]

pq = []

bags.sort()
stars.sort()
bags = deque(bags)

searched = 0
res = 0


while bags:
    now = bags.popleft()
    while searched <= n-1:
        if stars[searched][0] <= now:
            heapq.heappush(pq, stars[searched][1] * -1)
        else:
            break
        searched += 1
    if pq:
        res += heapq.heappop(pq) * -1

print(res)