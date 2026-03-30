import sys
import math
import re

input = sys.stdin.readline

if re.fullmatch(r'(100+1+|01)+', input().rstrip()):
    print("SUBMARINE")
else:
    print("NOISE")