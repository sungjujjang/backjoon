import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, b = input().rstrip().split()
b = int(b)

alpha = {
    "0" : 0,
    "1" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9
}
for i in range(10, 36):
    alpha[chr(i+55)] = i

total = 0
temp = 1
for i in range(len(n)-1, -1, -1):
    total += alpha[n[i]] * temp
    temp *= b

print(total)