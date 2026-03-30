import sys
import math
import re

input = sys.stdin.readline

T = int(input().rstrip())
ptn = re.compile(r'(100+1+|01)+')

for _ in range(T):
    string = input().rstrip()
    if ptn.fullmatch(string):
        print("YES")
    else:
        print("NO")
        