import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def to_sec(mp):
    h, m, s = mp
    return h*3600 + m*60 + s

start = to_sec(map(int, input().rstrip().split(":")))
end = to_sec(map(int, input().rstrip().split(":")))
t, k = map(int, input().rstrip().split())
k = (100 - k) / 100
t *= k

start += t

if start <= end:
    print(1)
else:
    print(0)
