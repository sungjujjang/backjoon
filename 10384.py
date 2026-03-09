import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input().rstrip())

def chk(n, l):
    for i in l:
        if i < n:
            return False
    return True

for i in range(1, n+1):
    alpha = [0] * 26
    st = input().rstrip()
    for s in st:
        if s.isalpha():
            alpha[ord(s.lower())-97] += 1
    alpha_sum = sum(alpha)
    # print(alpha_sum)
    if alpha_sum >= 26 * 3 and chk(3, alpha):
        print(f"Case {i}: Triple pangram!!!")
    elif alpha_sum >= 26 * 2 and chk(2, alpha):
        print(f"Case {i}: Double pangram!!")
    elif alpha_sum >= 26 and chk(1, alpha):
        print(f"Case {i}: Pangram!")
    else:
        print(f"Case {i}: Not a pangram")