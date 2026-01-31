import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

while True:
    a, b = map(int, input().rstrip().split())
    if a == b == 0:
        break
    if b % a == 0:
        print("factor")
    elif a % b == 0:
        print("multiple")
    else:
        print("neither")