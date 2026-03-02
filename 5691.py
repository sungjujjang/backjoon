import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

while True:
    a, b = map(int, input().rstrip().split())
    if a == b == 0:
        break
    print(a*2-b)