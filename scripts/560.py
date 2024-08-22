def xormul(a, b, c, mod):
    m = len(a)
    
    if m == 1:
        c[0] = a[0] * b[0] % mod
        return
    
    inv2 = pow(2, mod - 2, mod)  # Modular multiplicative inverse of 2 under mod
    
    ap, bp, an, bn = [], [], [], []
    mdiv = m // 2
    for i in range(mdiv):
        ap.append((a[i] + a[i + mdiv]) % mod)
        an.append((a[i] - a[i + mdiv] + mod) % mod)
    
    d0 = [0] * (mdiv)
    d1 = [0] * (mdiv)
    
    xormul(ap, ap, d0, mod)
    xormul(an, an, d1, mod)
    
    for i in range(mdiv):
        c[i] = (d0[i] + d1[i]) * inv2 % mod
        c[i + mdiv] = (d0[i] - d1[i] + mod) * inv2 % mod

from math import log2

n = 10**7
m = 10**7
mod = int(1e9 + 7)
nimber_size = int(log2(n) + 1)
n, m, nimber_size

from collections import Counter

nimbers = [[0 for  _ in range(2**nimber_size)] for _ in range(nimber_size)]
nimbers[0][1] = 1

s = [1 for _ in range(n)]
nimber = 1
for q in range(2, n):
    if s[q]:
        for i in range(q, n, q):
            if s[i]:
                if q == 2:
                    nimbers[0][0] += 1
                else:
                    nimbers[0][nimber] += 1
            s[i] = 0
        nimber += 1

for i in range(1, nimber_size):
    print(i)
    xormul(nimbers[i - 1], nimbers[i - 1], nimbers[i], mod)

base = nimbers[0]
left = m - 1
for i in range(nimber_size - 1, -1, -1):
    take = 1 << i
    while take <= left:
        left -= take
        print("Taking", take)
        res = [0 for  _ in range(2**nimber_size)]
        xormul(base, nimbers[i], res, mod)
        base = res.copy()
# print(base)
print(base[0] % mod)