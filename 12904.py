import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

S = list(input().rstrip())
T = list(input().rstrip())

while len(T) != len(S):
    if T[-1] == "A":
        T.pop()
    elif T[-1] == "B":
        T.pop()
        T.reverse()
    else:
        break

print(int(T==S))