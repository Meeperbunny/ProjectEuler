from sortedcontainers import SortedSet
from tqdm import tqdm

def sieve(n):
    s = [1 for _ in range(n + 1)]
    primes = []
    for q in range(2, n + 1):
        if s[q]:
            primes.append(q)
            for i in range(2 * q, n + 1, q):
                s[i] = 0
    return primes
primes = sieve(47)

limit = 10**16
c = SortedSet({1})
for i, p in enumerate(primes):
    print(i, len(primes), len(c))
    ta = SortedSet()
    for e in tqdm(c):
        for k in range(1, 100):
            num = e * p**k
            if num > limit:
                break
            ta.add(e * p**k)
        if e * p > limit:
            break
    c.update(ta)

T = 0
for e in tqdm(c):
    if e + 1 in c:
        T += e
print(T)