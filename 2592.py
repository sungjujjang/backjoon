import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

counts = [0] * 101
total = 0

for _ in range(10):
    n = int(input())
    counts[n//10] += 1
    total += n
    
print(total // 10)
print(counts.index(max(counts)) * 10)