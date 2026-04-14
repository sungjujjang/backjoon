w, h = map(int, input().split())
x, y, d = map(int, input().split())

map = [list(map(int, input().split())) for _ in range(w)]
cnt = 0

go = True
while go:
    go = False
    cnt += 1
    map[x][y] = 1
    for _ in range(4):
        if d == 0:
            if map[x][y-1] != 1:
                go = True
                y -= 1
                break
        elif d == 1:
            if map[x+1][y] != 1:
                go = True
                x += 1
                break
        elif d == 2:
            if map[x][y+1] != 1:
                go = True
                y += 1
                break
        else:
            if map[x-1][y] != 1:
                go = True
                x -= 1
                break
        d = (d+1) % 4

print(cnt)