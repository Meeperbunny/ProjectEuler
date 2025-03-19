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

N = 10**11
M = int(1e9+7)
t = 0
k = 1
while k <= N:
    k *= 2
    t += max(S(N // k, mod=M) - 1, 0)
print(t)
print(t % M)