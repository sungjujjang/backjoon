n = int(input())
dirs = input().split()

def check(x, y):
    if not (0 < x <= n):
        return False
    if not (0 < y <= n):
        return False
    return True

x, y = 1, 1
for dir in dirs:
    dx, dy = 0, 0
    if dir == "L":
        dx = -1
    if dir == "R":
        dx = 1
    if dir == "U":
        dy = -1
    if dir == "D":
        dy = 1
    if check(x+dx, y+dy):
        x += dx
        y += dy

print(y, x)