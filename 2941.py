import sys
import math
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

string = input().rstrip()
chars = ["dz=", "c=", "c-", "d-", "lj", "nj", "s=", "z="]

for c in chars:
    string = string.replace(c, "*")

print(len(string))
