from collections import Counter
def sieve(n):
    sieve = [1 for _ in range(n + 1)]
    primes = []
    for i in range(2, n + 1):
        if sieve[i]:
            primes.append(i)
            for q in range(2 * i, n + 1, i):
                sieve[q] = 0
    return primes
from tqdm import trange
from collections import Counter
def ans(N):
    pfc = Counter()
    print("Getting sivee")
    primes = sieve(N)
    print("getting Counts")
    for p in primes:
        k = 1
        pc = 0
        while p**k <= N:
            pc += N // p**k
            k += 1
        pfc[p] = pc
    T = 0
    mod = int(1e9 + 7)
    sqc = 0
    for sqc in trange(1, max(pfc.values()) + 1):
        t_c = Counter()
        to_rm = set()
        for e in pfc:
            if pfc[e] // sqc:
                t_c[e] = pfc[e] // sqc
            else:
                to_rm.add(e)
        for e in to_rm:
            del pfc[e]
        cc = 1
        if len(t_c) == 0:
            continue
        for e in t_c.values():
            cc *= (e + 1)
            cc %= mod
        cc -= 1
        T += cc
    return T % mod
print(ans(10**7))