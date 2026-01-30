import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

scores = []

for i in range(8):
    scores.append([int(input()), i+1])

scores.sort(key=lambda x: x[0])
scores.reverse()
total = 0
result = []
for i in range(5):
    total += scores[i][0]
    result.append(scores[i][1])
    
result.sort()
print(total)
print(*result)