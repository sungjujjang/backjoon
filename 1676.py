import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input().rstrip())
result = 0
while n >= 5:
    result += n//5
    n //= 5
print(result)