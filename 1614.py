import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

i = int(input().rstrip())
n = int(input().rstrip())

if i in [2, 3, 4]:
    if n % 2 == 0:
        print((n//2 * 8) + (i - 1))
    else:
        print((n//2 * 8) + (9 - i))
elif i == 1:
    print(8*n)
else:
    print(4 + 8*n)