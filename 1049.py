import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N, M = map(int, input().rstrip().split())
package_price = []
solo_price = []

for _ in range(M):
    a, b = map(int, input().rstrip().split())
    package_price.append(a)
    solo_price.append(b)

min_pacakage, min_solo = min(package_price), min(solo_price)

price = (N // 6) * min_pacakage
N %= 6
price += min(min_pacakage, N * min_solo)
print(price)