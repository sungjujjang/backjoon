import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N = int(input().rstrip())
starlist = [[" "] * N for _ in range(N)]

def print_list():
    for line in starlist:
        print(*line, sep="")

def stars(n, x, y):
    if n == 3:
        for i in range(3):
            for j in range(3):
                starlist[y+i][x+j] = "*"
        starlist[y+1][x+1] = " "
        return
    _n = n // 3
    stars(_n, x, y)
    stars(_n, x + _n, y)
    stars(_n, x + _n * 2, y)
    stars(_n, x, y + _n)
    stars(_n, x + _n * 2, y + _n)
    stars(_n, x, y + _n * 2)
    stars(_n, x + _n, y + _n * 2)
    stars(_n, x + _n * 2, y + _n * 2)

stars(N, 0, 0)
print_list()