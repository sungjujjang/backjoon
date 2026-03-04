import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input().rstrip())
a = set(map(int, input().rstrip().split()))

m = int(input().rstrip())
b = list(map(int, input().rstrip().split()))

for i in b:
    print(int(i in a), end=" ")