n = int(input())

arr = []

for i in range(n):
    tmp = input().split()
    arr.append((tmp[0], int(tmp[1])))
    
arr.sort(key= lambda x: x[1])

print(*[x[0] for x in arr], sep=" ")