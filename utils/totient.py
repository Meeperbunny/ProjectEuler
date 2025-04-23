def totient(n):
    tot = [1 for i in range(n + 1)]
    tot[0] = 0
    for p in range(2, n + 1):
        if tot[p] == 1:
            # is prime
            k = 1
            while True:
                b = p**k
                if b > n:
                    break
                j = p
                if k == 1:
                    j = p - 1
                for q in range(b, n + 1, b):
                    tot[q] *= j
                k += 1
    return tot

from functools import cache
@cache
def S(n, mod=None):
    """Computes the sum of the totient function from [1...n]"""
    if n == 1:
        return 1
    tri = (n * (n + 1) // 2)
    if mod:
        tri %= mod
    s1 = 0
    m = 2
    while m * m <= n:
        s1 += S(n // m)
        if mod:
            s1 %= mod
        m += 1
    s2 = 0
    d = 1
    while d * d <= n:
        if d != n // d:
            s2 += (n // d - n // (d + 1)) * S(d)
        if mod:
            s2 %= mod
        d += 1
    ans = (tri - s1 - s2)
    if mod:
        ans = (ans % mod + mod) % mod
    return ans