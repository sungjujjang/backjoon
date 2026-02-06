import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, k = map(int, input().rstrip().split())
before = []
after = []
for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
        if i != n//i:
            after.append(n//i)
        before.append(i)
after.reverse()
before += after
if len(before) < k:
    print(0)
else:
    print(before[k-1])