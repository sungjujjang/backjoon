import sys
import math

input = sys.stdin.readline

n, m, k, = map(int, input().rstrip().split())
a = list(map(int, input().rstrip().split()))

a.sort(reverse=True)

syc = a[0] * k + a[1]
res = syc * (m//(k+1)) + a[0] * (m%(k+1))
print(res)