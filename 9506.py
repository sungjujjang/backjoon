import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

while True:
    n = int(input().rstrip())
    if n == -1:
        break
    before = []
    after = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i != n//i:
                after.append(n//i)
            before.append(i)
    after.reverse()
    before += after
    del(before[-1])
    if sum(before) == n:
        print(f"{n} = ", end="")
        print(*before, sep=" + ")
    else:
        print(f"{n} is NOT perfect.")