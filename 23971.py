import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

i, j, n, m = map(int, input().rstrip().split())
print((math.ceil(i/(n+1)))*(math.ceil(j/(m+1))))