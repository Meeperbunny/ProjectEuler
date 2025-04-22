from tqdm import trange
from functools import cache
def tri(n):
    return n * (n - 1) // 2
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
T = 0
sqr = int(N**0.5)
for i in trange(1, sqr):
    T += i * S(N // i)
    l_v = N // i
for i in trange(l_v - 1, 0, -1):
    l = (N + i + 1) // (i + 1)
    u = N // i
    # print("D", i, l, u)
    cnts = u - l + 1
    T += (cnts * l + tri(cnts)) * S(i)
print(T % 998244353)