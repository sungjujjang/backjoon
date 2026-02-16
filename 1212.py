import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

print(bin(int(input().rstrip(), 8))[2:])