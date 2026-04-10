import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N = int(input().rstrip())

def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def wow_prime(len_, n_):
    if not is_prime(n_):
        return
    if len_ >= N:
        print(n_)
        return
    len_ += 1
    n_ *= 10
    for i in range(10):
        wow_prime(len_, n_+i)

for j in [2, 3, 5, 7]:
    wow_prime(1, j)