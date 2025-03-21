import math
from collections import Counter
from fractions import Fraction
from tqdm import tqdm

N = 10**9

def get_rad(r_1, r_2):
    prod = r_1 * r_2
    sqr = math.isqrt(prod)
    if sqr * sqr == prod:
        t = r_1 + r_2 + 2 * sqr
        if t != 0 and prod % t == 0:
            return prod // t
    return 0

def sieve(n):
    s = [1]*(n+1)
    primes = []
    for q in range(2, n+1):
        if s[q]:
            primes.append(q)
            for i in range(2*q, n+1, q):
                s[i] = 0
    return primes

def moebius(n):
    primes = sieve(n)
    m = [1]*(n+1)
    for p in primes:
        for i in range(p, n+1, p):
            m[i] *= -1
        for i in range(p*p, n+1, p*p):
            m[i] = 0
    return m

M = moebius(int(N**0.5+1))
tri = lambda x: (x * x + x) // 2

def num_squarefree(n):
    tot = 0
    # Using integer arithmetic where possible
    for i in range(1, int(n**0.5+1)):
        ni = n // (i*i)
        tot += (i * i) * ni * M[i] * (ni + 1)
    return tot / 2

T = 0

for a in tqdm(range(0, int(N**0.5+1))):
    if a * a > N:
        break
    b = 0
    while b * b <= N:
        b += 1
        r_a = a * a
        r_c = b * b
        
        if (b - a) == 0:
            continue
        r_b = a * a * b * b // (b - a)**2
        if r_b < r_a:
            continue
        if r_a == r_b and r_a != 4:
            continue
        if get_rad(r_a, r_b) == r_c:
            if r_a <= N and r_b <= N:
                S = r_a + r_b + r_c
                n_sq = num_squarefree(N // max(r_a, r_b))
                if r_a == 4:
                    n_sq = tri(N // 4)
                T += int(n_sq * S)

print(T)
