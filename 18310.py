import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input().rstrip())
a_ = list(map(int, input().rstrip().split()))
a_.sort()

print(a_[(n-1)//2])