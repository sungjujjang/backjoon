import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())

for i in range(0, n):
    print("*" * (i+1))
    
for j in range(n-1, 0, -1):
    print("*" * (j))