def get_gcd(a, b):
    if b == 0:
        return a
    return get_gcd(b, a % b)

A, B = map(int, input().split())

print(get_gcd(A, B))
