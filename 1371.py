import sys
import math

input = sys.stdin.read
sys.setrecursionlimit(1000000)

word = [0] * 26

lines = input().rstrip()
for line in lines:
    for s in line:
        if 'a' <= s <= 'z':
            word[ord(s) - 97] += 1

max_n = max(word)
for i in range(26):
    if word[i] == max_n:
        print(chr(i + 97), end="")