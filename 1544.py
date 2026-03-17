import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input().rstrip())
cnt = 0
li = []

for i in range(n):
    t = True
    sri = input().rstrip()
    for string in li:
        if sri in string and len(sri)*2 == len(string):
            t = False
            break
    if t:
        cnt += 1
        li.append(sri*2)

print(cnt)