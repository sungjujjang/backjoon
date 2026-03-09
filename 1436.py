import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

i = 666
c = 0

n = int(input().rstrip())

while True:
    nstr = str(i)
    if "666" in nstr:
        c += 1
    
    if c == n:
        print(nstr)
        break
    
    i += 1