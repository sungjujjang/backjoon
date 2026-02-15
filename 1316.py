import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())
count = 0
for _ in range(n):
    string = input().rstrip()
    alpha = []
    ok = True
    for i in range(len(string)):
        if string[i] in alpha:
            if string[i-1] == string[i]:
                continue
            ok = False
            break
        else:
            alpha.append(string[i])
    
    if ok:
        count += 1
        
print(count)