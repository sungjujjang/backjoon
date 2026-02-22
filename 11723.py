import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

m = int(input().rstrip())
main = set()
al = set([i for i in range(1, 21)])
for _ in range(m):
    cmd = input().rstrip().split()
    if cmd[0] == "add":
        main.add(int(cmd[1]))
    elif cmd[0] == "remove":
        main.discard(int(cmd[1]))
    elif cmd[0] == "check":
        print(int(int(cmd[1]) in main))
    elif cmd[0] == "toggle":
        if int(cmd[1]) in main:
            main.discard(int(cmd[1]))
        else:
            main.add(int(cmd[1]))
    elif cmd[0] == "all":
        main = al.copy()
    else:
        main = set()