import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input().rstrip())
a = list(enumerate(map(int, input().rstrip().rsplit())))

a_sort = sorted(a, key=lambda x: x[1])
res = [0] * n

for i in range(n):
    res[a_sort[i][0]] = i

print(*res)