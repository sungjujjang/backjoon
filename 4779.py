import sys
import math

input = sys.stdin.read
sys.setrecursionlimit(1000000)

a = []

def kantoa(start, end): # 0 idx problem
    global a
    offset = (end - start + 1) // 3
    if offset == 0:
        return
    a[start+offset-1:(start+offset*2)-1] = [" "] * offset
    kantoa(start, start+offset)
    kantoa(start+offset*2, end)
    

ns = map(int, input().splitlines())
for n in ns:
    nel_ = 3**n
    a = ["-"] * nel_
    kantoa(1, nel_)
    print(*a, sep="")