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
        if D[p] > D[p - 1]:  # this indicates that p is prime
            # For each v in V with v >= p*p, update D[v]
            for v in V:
                if v < p * p:
                    break
                D[v] -= D[v // p] - D[p - 1]
    return D[n]