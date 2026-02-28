import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

r, c, zr, zc = map(int, input().rstrip().split())
for i in range(r):
    st = input().rstrip()
    new_st = ""
    for s in st:
        new_st += s*zc
    print((new_st+"\n")*zr, end="")