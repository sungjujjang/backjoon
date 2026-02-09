import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

people = set()
count = 0
n = int(input())
for _ in range(n):
    s = input().rstrip()
    if s == "ENTER":
        people = set()
    else:
        if s not in people:
            count += 1
            people.add(s)

print(count)