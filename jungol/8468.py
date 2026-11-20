from collections import deque

N, K = map(int, input().split())
a = list(map(int, input().split()))

max_deque = deque()
min_deque = deque()

start = 0
max_len = 0

for end in range(N):
    while max_deque and a[max_deque[-1]] < a[end]:
        max_deque.pop()

    max_deque.append(end)

    while min_deque and a[min_deque[-1]] > a[end]:
        min_deque.pop()

    min_deque.append(end)

    while a[max_deque[0]] - a[min_deque[0]] > K:
        start += 1

        if max_deque[0] < start:
            max_deque.popleft()

        if min_deque[0] < start:
            min_deque.popleft()

    max_len = max(max_len, end - start + 1)

print(max_len)
