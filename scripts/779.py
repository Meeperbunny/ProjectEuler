from fractions import Fraction
from tqdm import tqdm
from decimal import Decimal, getcontext

getcontext().prec = 36

def sieve(n):
    s = [1 for _ in range(n + 1)]
    primes = []
    for q in range(2, n + 1):
        if s[q]:
            primes.append(q)
            for i in range(2 * q, n + 1, q):
                s[i] = 0
    return primes

def amnt(n):
    primes = sieve(n)
    s, la = Decimal(1), Decimal(1)
    ret = []
    for p in primes:
        p = Decimal(p)
        s = s * (1 - (1 / p))
        ret.append((p, la - s))
        la = s
    return ret

ans = 0
n, k, pm = 60_000, 1_000, 1_000
A = amnt(n)
ans = Decimal(0)
i = 0
for p, R in tqdm(A):
    for K in range(1, k + 1):
        ra = R
        for po in range(1, pm):
            curr = ra - (ra/p)
            ra = ra / p
            d = curr * (po - 1) / p**K
            if po != 1 and d 
            ans += d
print(ans)