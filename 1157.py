import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

word = input().rstrip().lower()
alpha = [0] * 26

for s in word:
    alpha[ord(s)-97] += 1

max_count = max(alpha)
if alpha.count(max_count) > 1:
    print("?")
else:
    print(chr(alpha.index(max_count)+97).upper())