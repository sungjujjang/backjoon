import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

y1, m1, d1, t1, p1 = input().rstrip().split()
y2, m2, d2, t2, p2 = input().rstrip().split()

y1, m1, d1, y2, m2, d2 = map(int, [y1, m1, d1, y2, m2, d2])
t1, p1, t2, p2 = map(float, [t1, p1, t2, p2])

now = (y1-1)*360 + (m1-1)*30 + d1
target = (y2-1)*360 + (m2-1)*30 + d2

now += (target - now) * -1
y, m, d = (now - 1) // 360 + 1, ((now - 1) % 360) // 30 + 1, ((now - 1) % 360) % 30 + 1
t = t1 + (t2 - t1) * -1
p = p1 + (p2 - p1) * -1
print("%d %d %d %.3f %.3f" %(y, m, d, t, p))