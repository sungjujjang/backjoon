def get_gcd(a, b):
    if b == 0:
        return a
    return get_gcd(b, a % b)

def get_lcm(a, b):
    return a * b / get_gcd(a, b)

A, B = map(int, input().split())
print(int(get_lcm(A, B)))

