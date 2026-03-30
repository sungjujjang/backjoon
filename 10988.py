import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

s = input().rstrip()
if len(s) % 2 == 1:
    print(1 if list(s[:(len(s)//2)+1]) == list(reversed(s[len(s)//2:])) else 0)
else:
    print(1 if list(s[:(len(s)//2)]) == list(reversed(s[len(s)//2:])) else 0)