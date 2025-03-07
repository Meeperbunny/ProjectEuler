def totient(n):
    tot = [1 for i in range(n + 1)]
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

tot = totient(1005000)

from math import gcd

def bz_c(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    
    return old_s, old_t

from math import gcd, lcm

def g(a, m, b, n):
    gc = gcd(m, n)
    M = lcm(m, n)
    if a % gc != b % gc:
        return 0
    u, v = bz_c(m, n)
    x = (a * v * n + b * u * m) // gc
    return ((x % M) + M) % M

s = 0
for n in range(1000000, 1005000):
    if n % 100 == 0:
        print(n)
    for m in range(n + 1, 1005000):
        s += g(tot[n], n, tot[m], m)
print(s)