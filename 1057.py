import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, a, b = map(int, input().rstrip().split())

c = 0
while a != b:
    c += 1
    a = a//2 if a % 2 == 0 else a//2+1
    b = b//2 if b % 2 == 0 else b//2+1

print(c)

# print(new_tor)
# print(-1)


#        8                   9
#    1       8        9            13
#  1   3   5   8   9    11     13    15  
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16

# 9 - 5 - 3 - 2
# 8 - 4 - 2 - 1