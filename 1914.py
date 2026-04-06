import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input().rstrip())

def hanoi(n, start, tmp, end):
    if n <= 1:
        print(start, end)
        return
    hanoi(n-1, start, end, tmp)
    print(start, end)
    hanoi(n-1, tmp, start, end)
    
print(2**n-1)
if n <= 20:
    hanoi(n, 1, 2, 3)