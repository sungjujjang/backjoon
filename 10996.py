import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input().rstrip())

for _ in range(n):
    print('* ' * (n//2 + n%2))
    print(' *' * (n//2))