import sys
import math
from collections import deque

input = sys.stdin.readline

# def cnt_sort(li):
#     res = [0] * 1000001
#     for i in li:
#         res[i] += 1
#     result = []
#     for i in range(1000000, 0, -1):
#         for _ in range(res[i]):
#             result.append(i)
#     return result

N = int(input().rstrip())
Ns = list(map(int, input().rstrip().split()))
M = int(input().rstrip())
Ms = list(map(int, input().rstrip().split()))

Ns.sort(reverse=True)
Ms.sort(reverse=True)

# crains = cnt_sort(Ns)
# boxes = cnt_sort(Ms)

crains = Ns
boxes = Ms
moved = [False] * M
pos = [0] * N
cnt = 0

result = 0

if boxes[0] > crains[0]:
    print(-1)
    sys.exit()

while cnt < M:
    for i in range(N):
        while pos[i] < M:
            if not moved[pos[i]] and crains[i] >= boxes[pos[i]]:
                moved[pos[i]] = True
                cnt += 1
                pos[i] += 1
                break
            pos[i] += 1
    result += 1

print(result)