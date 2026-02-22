import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, m = map(int, input().rstrip().split())
passwords = {}
for _ in range(n):
    site, password = input().rstrip().split()
    passwords[site] = password
for _ in range(m):
    site = input().rstrip()
    print(passwords.get(site))