import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

w, h = map(int, input().rstrip().split())
print('%.1f' %(w*h/2))