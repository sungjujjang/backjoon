n = int(input())
res = 0

h, m, s = 0, 0, 0
while not (h==n and m==59 and s==59):
    st = f'{h}{m}{s}'
    if "3" in st:
        res += 1
    s += 1
    if s == 60:
        s = 0
        m += 1
    if m == 60:
        m = 0
        h += 1
        
print(res)