import sys
import math
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

t = int(input().rstrip())
for _ in range(t):
    n, m = map(int, input().rstrip().split())
    ift = list(map(int, input().rstrip().split()))
    
    for i in range(n):
        ift[i] = (i, ift[i])
    
    quque = deque(ift)
    count = 0
    max_ = max(quque, default=(0 ,0), key=lambda x: x[1])
    while quque:
        tmp = quque.popleft()
        if max_[1] > tmp[1]:
            quque.append(tmp)
            continue
        count += 1
        if tmp[0] == m:
            print(count)
        if tmp[0] == max_[0]:
            max_ = max(quque, default=(0 ,0), key=lambda x: x[1])
