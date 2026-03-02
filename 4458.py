import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input().rstrip())
for _ in range(n):
    s = input().rstrip()
    print(s[0].upper()+s[1:])