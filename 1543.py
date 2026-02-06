import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

string = input().rstrip()
text = input().rstrip()

print(string.count(text))