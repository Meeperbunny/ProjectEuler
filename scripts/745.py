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

def solve(N):
    M = moebius(int(N**0.5+1))

    def num_squarefree(n):
        tot = 0
        for i in range(1, int(n**0.5+1)):
            tot += (n // (i*i)) * M[i]
        return tot

    i = 1
    ans = 0
    while i * i <= N:
        sq = i * i

        new_n = N // sq
        sq_cnt = new_n = num_squarefree(new_n)
        cont = sq_cnt * sq

        ans += cont
        
        i += 1
    return ans
print(solve(10**14) % int(10**9+7))