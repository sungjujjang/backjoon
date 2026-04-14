di = input()

def check(x, y):
    if not (0 < x <= 8):
        return False
    if not (0 < y <= 8):
        return False
    return True

x, y = int(ord(di[0])-96), int(di[1])
dirs = [(2, 1), (2, -1), (-2 ,1), (-2 ,-1), 
        (1, 2), (-1, 2), (1, -2), (-1, -2)]

cnt = 0
for dx, dy in dirs:
    if check(x+dx, y+dy):
        cnt += 1

print(cnt)