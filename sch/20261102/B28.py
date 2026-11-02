import sys
sys.setrecursionlimit(1000001)

N = int(input())
mod = 1000000007

memo = [0] * (N+1)
def fibo(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if memo[n] != 0:
        return memo[n]
    rs = ((fibo(n - 1) % mod) + (fibo(n - 2) % mod)) % mod
    memo[n] = rs
    return rs

print(fibo(N))
