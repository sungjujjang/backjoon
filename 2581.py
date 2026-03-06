import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def isprime(n):
    if n < 2:
        return False
    for i_ in range(2, int(math.sqrt(n))+1):
        if n % i_ == 0:
            return False
    return True

m = int(input().rstrip())
n = int(input().rstrip())

a = []
min_ = float("inf")
for i in range(m, n+1):
    if isprime(i):
        a.append(i)
        min_ = min(min_, i)

if len(a) == 0:
    print(-1)
    exit(0)

print(sum(a))
print(min_)