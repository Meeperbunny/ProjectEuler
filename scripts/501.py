from utils.sieve import sieve
primes = sieve(10**6)
from tqdm import tqdm
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
    return D
N = 10**12
D = pi(N)
# p^7
T = 0
for p in (primes):
    if p**7 < N:
        T += 1
    else:
        break
for i, p in (enumerate(primes)):
    bp = p**3
    if bp > N:
        break
    # Find the number of primes that this is good for. If our prime is in it, subtract 1.
    goodprimes = D[N // bp]
    if goodprimes > i:
        goodprimes -= 1
    # print("G", p, N // bp, goodprimes)
    T += goodprimes

for i, p1 in (enumerate(primes)):
    for q, p2 in enumerate(primes[i+1:]):
        num = p1 * p2
        d = N // num
        if d <= p2:
            break
        # if  pi(d) - (i + q + 2):
        #     print(p1, p2, d, pi(d), (q + 1), pi(d) - (i + q + 2))
        T += D[d] - (i + q + 2)
print(T)