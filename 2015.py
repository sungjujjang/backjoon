import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, k = map(int, input().rstrip().split())
a = list(map(int, input().rstrip().split()))

s = {
    0: 1
}

result = 0
sum_ = 0
for i in range(n):
    sum_ += a[i]
    result += s.get(sum_-k, 0)
    s[sum_] = s.get(sum_, 0) + 1

print(result)