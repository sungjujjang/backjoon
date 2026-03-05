import sys
from collections import deque

input = sys.stdin.readline

line = input().strip()

if '.' in line:
    a, b = line.split('.')
    if b not in ['0', '5']:
        print(-1)
        exit()
    target = int(a) * 2 + (1 if b == '5' else 0)
else:
    target = int(line) * 2

MOD = 126
limit = MOD * 50

moves = [18, 14, 9, -4]

doc = {0: 0}
queue = deque([0])

while queue:
    temp = queue.popleft()
    d = doc[temp]

    for i in moves:
        next_ = temp + i
        if 0 <= next_ <= limit:
            if next_ not in doc:
                doc[next_] = d + 1
                queue.append(next_)

if target <= limit:
    print(doc.get(target, -1))
else:
    result = float('inf')
    for v, i in doc.items():
        if v <= target and (target - v) % MOD == 0:
            extra = (target - v) // MOD
            result = min(result, i + extra * 7) # 18 * 7

    print(result if result != float('inf') else -1)