import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

numbers = [int(input()) for i in range(5)]
numbers.sort()
print(sum(numbers) // 5)
print(numbers[2])