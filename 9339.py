import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

t = int(input().rstrip())

for i in range(t):
    n = int(input().rstrip())
    an = set(map(int, input().rstrip().split()))
    k = int(input().rstrip())

    # 360 분
    cnt = 0
    min_num = float("inf")
    min_m = float("inf")

    for _ in range(k):
        kn, h, m = map(int, input().rstrip().split())
        ms = h*60 + m
        if kn in an and 0 <= ms <= 360:
            if min_m > ms:
                min_m = ms
                min_num = kn
            cnt += 1

    print(min_num, cnt)
    