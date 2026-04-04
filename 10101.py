import sys
import math

input = sys.stdin.read
sys.setrecursionlimit(1000000)

tri = list(map(int, input().rsplit()))
tri.sort()

if sum(tri) != 180:
    print("Error")
else:
    if tri[0] == tri[1] == tri[2]:
        print("Equilateral")
    elif tri[0] == tri[1] or tri[1] == tri[2]:
        print("Isosceles")
    else:
        print("Scalene")