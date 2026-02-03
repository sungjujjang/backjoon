import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)


while True:
    a, b, c = sorted(list(map(int, input().split())))

    if a == b == c:
        if a == 0:
            break
        print("Equilateral")
    elif c >= a+b:
        print("Invalid")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")