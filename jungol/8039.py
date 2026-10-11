import heapq

N, Q = list(map(int, input().split()))
status = dict()
p = [0] * (N + 1)
base = [i for i in range(1, N+1)]
heapq.heapify(base)
status[0] = base

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        p[query[1]] += query[2]
        h = status.get(p[query[1]], [])
        heapq.heappush(h, query[1])
        status[p[query[1]]] = h
    elif query[0] == 1:
        h = status.get(query[1], [])[:]
        rst = []
        while h:
            tmp = heapq.heappop(h)
            if p[tmp] == query[1]:
                rst.append(str(tmp))
        if rst:
            print(" ".join(rst))
        else:
            print("None")
