# Sieve then construct pi(i), prime counting function
def prime_count(n):
    s = [1 for _ in range(n + 1)]
    pi = [0 for _ in range(n + 1)]
    s[0], s[1] = 0, 0
    primes = []
    for q in range(2, n + 1):
        if s[q]:
            primes.append(q)
            for i in range(2 * q, n + 1, q):
                s[i] = 0
    
    for i in range(1, n + 1):
        pi[i] = pi[i - 1] + s[i]
    return pi

def pi(n):
    r = int(n ** 0.5)
    assert r * r <= n and (r + 1) ** 2 > n
    V = [n // i for i in range(1, r + 1)]
    V += list(range(V[-1] - 1, 0, -1))
    D = {v: v - 1 for v in V}
    for p in range(2, r + 1):
        if D[p] > D[p - 1]:
            for v in V:
                if v < p * p:
                    break
                D[v] -= D[v // p] - D[p - 1]
    return D[n]

# Base recurrence for Lucy Hedgehog
@cache
def S(v, p):
    if p <= 1:
        return v - 1
    if p not in pset:
        return S(v, p - 1)
    if p * p > v:
        return S(v, p - 1)
    return S(v, p - 1) - (S(v // p, p - 1) - S(p - 1, p - 1))
def PI(N):
    return S(N, int(N**0.5))