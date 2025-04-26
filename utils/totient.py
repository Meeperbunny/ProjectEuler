def totient(n):
    tot = [1 for i in range(n + 1)]
    tot[0] = 0
    for p in range(2, n + 1):
        if tot[p] == 1:
            # is prime
            k = 1
            while True:
                b = p**k
                if b > n:
                    break
                j = p
                if k == 1:
                    j = p - 1
                for q in range(b, n + 1, b):
                    tot[q] *= j
                k += 1
    return tot

from functools import cache
@cache
def S(n, mod=None):
    """Computes the sum of the totient function from [1...n]"""
    if n == 1:
        return 1
    tri = (n * (n + 1) // 2)
    if mod:
        tri %= mod
    s1 = 0
    m = 2
    while m * m <= n:
        s1 += S(n // m)
        if mod:
            s1 %= mod
        m += 1
    s2 = 0
    d = 1
    while d * d <= n:
        if d != n // d:
            s2 += (n // d - n // (d + 1)) * S(d)
        if mod:
            s2 %= mod
        d += 1
    ans = (tri - s1 - s2)
    if mod:
        ans = (ans % mod + mod) % mod
    return ans

from tqdm import trange, tqdm
from collections import Counter
from utils.miller_rabin import miller_rabin
from utils.prime_factors import pfs

def inverse_totient(num):
    def maxPow(n, p):
        k = 0
        while n % p**(k + 1) == 0:
            k += 1
        return k
    mc = Counter(pfs(num))
    def ntoi(n):
        t = 0
        for p in mc:
            mp = maxPow(n, p)
            if mp > mc[p]:
                return -1
            t = t * (mc[p] + 1) + mp
            n //= p**mp
        if n != 1:
            return -1
        return t
    bm = 1
    for e in mc.values():
        bm *= e + 1
    def iton(i):
        bb = 1
        t = 1
        for p in reversed(mc):
            # cc[p] = (i // bb) % (mc[p] + 1)
            t *= p**((i // bb) % (mc[p] + 1))
            bb *= (mc[p] + 1)
        # return cc
        return t
    
    C = pfs(num)
    C
    v = set()
    for i in trange(0, 2**len(C)):
        cm = 1
        for q in range(len(C)):
            if (i >> q) & 1:
                cm *= C[q]
        if miller_rabin(cm + 1, k=10):
            v.add(cm + 1)
    
    mnum = ntoi(num)
    lk = [set() for _ in range(mnum + 1)]
    lk[0] = set({1})
    for p in tqdm(reversed(sorted(v))):
        # print("Working on p = {}".format(p))
        nlk = [set() for _ in range(mnum + 1)]
        k = 0
        ctot = 1
        m = 1
        while True:
            ci = ntoi(ctot)
            if ci == -1:
                break
            # print(p, ctot, ci)
            # Iter through each lk and mult myself with each, adding through.
            for q in range(0, mnum + 1):
                ttot = iton(q) # Get current tot
                ntot = ctot * ttot
                # Get index of new totient
                utot = ntoi(ntot)
                if utot != -1: # If new totient is valid, then propagate.
                    for el in lk[q]:
                        nlk[utot].add(el * m)
                    
            k += 1
            if k == 1:
                ctot *= p - 1
            else:
                ctot *= p
            m *= p
        for i in range(0, mnum + 1):
            lk[i].update(nlk[i])
    mind = ntoi(num)
    # print("Len of {}".format(len(lk[mind])))
    return sorted(lk[mind])