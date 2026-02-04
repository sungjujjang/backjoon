import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

aeiou = ['a', 'e', 'i', 'o', 'u']

while True:
    string = input().rstrip()
    if string == "#":
        break
    count = 0
    for s in string:
        if s.lower() in aeiou:
            count += 1
    print(count)