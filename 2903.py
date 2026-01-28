import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())
print((1+2**n)**2)