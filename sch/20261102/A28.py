N = int(input())

total = 0
for _ in range(N):
    T, A = input().split()
    if T == "*":
        total *= int(A)
    elif T == "+":
        total += int(A)
    else:
        total -= int(A)
    print(total % 10000)
