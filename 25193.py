import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input().rstrip())
schedul = input()

chiken = schedul.count("C")
n -= chiken

print((chiken+n)//(n+1))