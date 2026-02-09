import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())
a, b = map(int, input().split())

print(min(n, (a + 2*b)//2))