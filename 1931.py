import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input().rstrip())
timetable = []
for _ in range(n):
    s, e = map(int, input().rstrip().split())
    timetable.append((s, e, e-s))

timetable.sort(key=lambda x: (x[1], x[0]))

i = 0
prev = -1
cnt = 0
while i < n:
    now = timetable[i]
    if now[0] >= prev:
        cnt += 1
        prev = now[1]
        # print(now)
    i += 1

print(cnt)