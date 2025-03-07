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