import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, m = map(int, input().rstrip().split())
poket = dict()
poket_list = []

for i in range(1, n+1):
    s = input().rstrip()
    poket[s] = i
    poket_list.append(s)

for _ in range(m):
    s = input().rstrip()
    if s.isdigit():
        print(poket_list[int(s)-1])
    else:
        print(poket[s])