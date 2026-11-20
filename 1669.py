import sys
import math

X, Y = map(int, sys.stdin.readline().split())

D = Y - X

if D == 0:
    print(0)
else:
    n = math.isqrt(D)

    if n * n >= D:
        print(2 * n - 1)
    else:
        print(2 * n)