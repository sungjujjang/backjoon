n, k = map(int, input().split())

def inserting(arr, n):
    for i in range(0, len(arr)):
        if arr[i] >= n:
            arr.insert(i, n)
            break
    return arr

def inserting_reverse(arr, n):
    for i in range(0, len(arr)):
        if arr[i] <= n:
            arr.insert(i, n)
            break
    return arr

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=True)
b.sort()

i = 0
while a[-1] < b[-1] and k > i:
    i += 1
    print(a, b)
    a_ = a.pop()
    b_ = b.pop()
    b = inserting(b, a_)
    a = inserting_reverse(a, b_)

print(sum(a))