import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input().rstrip())
a = list(map(int, input().rstrip().split()))

print(a.count(n))