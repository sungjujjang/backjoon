import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

nums = list(map(int, input().rstrip().split()))
n = min(nums)

while True:
    cnt = 0
    for i in nums:
        if n % i == 0:
            cnt += 1
    if cnt >= 3:
        print(n)
        break
    n += 1