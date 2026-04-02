import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

schools = {
    "animal": "Panthera tigris",
    "tree": "Pinus densiflora",
    "flower": "Forsythia koreana"
}

while True:
    s = input().rstrip()
    if s == "end":
        break
    print(schools[s])