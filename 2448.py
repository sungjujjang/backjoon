import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input().rstrip())
stars = [[" "] * (n * 2 - 1) for _ in range(n)]

def draw_last(i, j): # i 행 j 열
    global stars
    stars[i][j] = "*"
    stars[i+1][j+1] = "*"
    stars[i+1][j-1] = "*"
    for _i in range(5):
        stars[i+2][j-2+_i] = "*"
        
def draw_star(i, j, _n): # i 행 j 열
    # print(i, j, _n)
    if _n <= 3:
        draw_last(i, j)
        return
    _n = _n//2
    draw_star(i, j, _n)
    draw_star(i + _n, j + _n, _n)
    draw_star(i + _n, j - _n, _n)
    
# 24번째 별
draw_star(0, n-1, n)
for st in stars:
    print(*st, sep="")