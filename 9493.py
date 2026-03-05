import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

while True:
    m, a, b = map(int, input().rstrip().split())
    if m == a == b == 0:
        break
    a_h, b_h = m/a*3600, m/b*3600
    min_h = round(abs(a_h - b_h))
    h = min_h // 3600
    m_ = (min_h % 3600) // 60
    s = min_h % 60

    print(f"{h}:{m_:02d}:{s:02d}")