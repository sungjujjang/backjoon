import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())
board = [[0] * 101 for _ in range(101)]
for _ in range(n):
    x, y = map(int, input().split())
    for dx in range(x, x+10):
        for dy in range(y, y+10):
            board[dx][dy] = 1

print(sum(map(sum, board)))