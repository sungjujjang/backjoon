from collections import deque
import sys

# [[i, j], hop, ['A', 'B', ...]]
input = sys.stdin.readline

R, C = map(int, input().split())
ml = []
max_hop = -1

def checksum(i, j, letters):
    if i > (R-1) or i < 0:
        return False
    if j > (C-1) or j < 0:
        return False
    if ml[i][j] in letters:
        return False
    return True

for _ in range(R):
    tmp = list(str(input()))
    ml.append(tmp)

stack = deque([[(0, 0), 1, set([ml[0][0]])]])
dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

while stack:
    direction, hop, letters = stack.pop()
    max_hop = max(hop, max_hop)
    x, y = direction
    for dx, dy in dirs:
        i = x + dx
        j = y + dy
        if checksum(i, j, letters):
            stack.append([[i, j], hop+1, letters|{ml[i][j]}])

print(max_hop)
