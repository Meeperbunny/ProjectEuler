def sieve(n):
    s = [1 for _ in range(n + 1)]
    primes = []
    for q in range(2, n + 1):
        if s[q]:
            primes.append(q)
            for i in range(2 * q, n + 1, q):
                s[i] = 0
    return primes
primes = sieve(10**6)
from functools import cache
def cnts(N, p):
    k = 0
    c = []
    while p**k <= N:
        c.append(N // (p**k))
        k += 1
    rt = 0
    for i in range(0, len(c)):
        c[len(c) - i - 1] -= rt
        rt += c[len(c) - i - 1]
    return c
@cache
def pi(n):
    r = int(n ** 0.5)
    assert r * r <= n and (r + 1) ** 2 > n
    V = [n // i for i in range(1, r + 1)]
    V += list(range(V[-1] - 1, 0, -1))
    D = {v: v - 1 for v in V}
    for p in range(2, r + 1):
        if D[p] > D[p - 1]:  # this indicates that p is prime
            # For each v in V with v >= p*p, update D[v]
            for v in V:
                if v < p * p:
                    break
                D[v] -= D[v // p] - D[p - 1]
    return D[n]
from tqdm import *
N = 10**12
A = 0
r = int(N ** 0.5)
assert r * r <= N and (r + 1) ** 2 > N
V = [N // i for i in range(1, r + 1)]
V += list(range(V[-1] - 1, 0, -1))
D = {v: v - 1 for v in V}
for p in tqdm(range(2, r + 1)):
    if D[p] > D[p - 1]:  # this indicates that p is prime
        # For each v in V with v >= p*p, update D[v]
        for v in V:
            if v < p * p:
                break
            D[v] -= D[v // p] - D[p - 1]
for p in tqdm(primes):
    if p * p >= N:
        break
    else:
        T = 0
        c = cnts(N, p)
        l = 0
        lt = 0
        for i, e in enumerate(c):
            T += e * lt
            l += e
            lt += l
        T *= 2
        # print("PRime", p, "is adding", T)
        A += T
for i in tqdm(range(int(N**0.5-1), 0, -1)):
    lower = (N + 1 + i) // (i + 1)
    upper = (N) // (i)
    if upper < lower:
        continue
    # print("IUL", i, upper, lower)
    to_add = (N - i) * i
    cnt = D[upper] - D[lower - 1]
    # print(upper, lower - 1)
    # print("CC", cnt, to_add, cnt * to_add)
    A += 2 * cnt * to_add
print(A, A % int(1e9+7))