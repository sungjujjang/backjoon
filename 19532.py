import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

a, b, c, d, e, f = map(int, input().rstrip().split())
print(
    int((c*e - b*f) / (a*e - b*d)), 
    int((c*d - a*f) / (b*d - a*e))
)