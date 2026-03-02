import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input().rstrip())
a = list(map(int, input().rstrip().split()))
# used = [False] * n

# count = 0
# for i in range(n):
#     if not used[i]:
#         count += 1
#         temp = [a[i]]
#         for j in range(i+1, n):
#             if not used[j] and temp[-1] < a[j]:
#                 used[j] = True
#                 temp.append(a[j])

count = 0
temp = set(a)
max_li = []
for i in a:
    max_li.append(a.count(i))

print(max(max_li))