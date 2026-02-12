import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def next_per(arr):
    n = len(arr)
    pivot = -1
    for i in range(n-2, -1, -1):
        if arr[i] < arr[i+1]:
            pivot = i
            break
    if pivot == -1:
        return False

    for j in range(n-1, pivot, -1):
        if arr[j] > arr[pivot]:
            arr[pivot], arr[j] = arr[j], arr[pivot]
            break

    arr[pivot+1:] = reversed(arr[pivot+1:])
    return arr

n = int(input().rstrip())
sun = list(range(1, n+1))
while sun:
    print(*sun)
    sun = next_per(sun)