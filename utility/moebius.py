def sieve(n):
    s = [1 for _ in range(n + 1)]
    primes = []
    for q in range(2, n + 1):
        if s[q]:
            primes.append(q)
            for i in range(2 * q, n + 1, q):
                s[i] = 0
    return primes

def moebius(n):
    primes = sieve(n)
    m = [1 for _ in range(n + 1)]
    for p in primes:
        for i in range(p, n + 1, p):
            m[i] *= -1
        for i in range(p * p, n + 1, p * p):
            m[i] = 0
    return m