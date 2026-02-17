import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())

height_count = [0] * 257

min_h = 256
max_h = 0

for _ in range(n):
    row = list(map(int, input().split()))
    for h in row:
        height_count[h] += 1
        min_h = min(min_h, h)
        max_h = max(max_h, h)

bt = 999999999999999999
bh = 0

for t in range(min_h, max_h + 1):
    remove = 0
    add = 0

    for h in range(257):
        if height_count[h] == 0:
            continue
        
        if h > t:
            remove += (h - t) * height_count[h]
        elif h < t:
            add += (t - h) * height_count[h]

    if remove + b < add:
        continue

    time = remove * 2 + add

    if time < bt or (time == bt and t > bh):
        bt = time
        bh = t

print(bt, bh)