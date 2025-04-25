from utils.sieve import sieve
from itertools import combinations
from tqdm import tqdm
from fractions import Fraction
from utils.prime_factors import pfs
K = 33
rprimes = sieve(600)
for e in sieve(K):
    rprimes.remove(e)
valid_psets = []
for i in range(1, 4 + 1):
    print(i)
    valid_psets += list(combinations(rprimes, i))
len(valid_psets)
valid_psets.append(tuple())
primes = sieve(K)
print(len(primes))

inset = [(1, 1)]
N = 10**18
for p in primes:
    print(p, len(inset))
    k = 0
    newset = []
    modifier = 1
    while p**k <= N:
        if p >= 3 and k >= 8:
            break
        if p >= 5 and k >= 6:
            break
        if p >= 7 and k >= 4:
            break
        for e, l in inset:
            if e * p**k < N:
                newset.append((e * p**k, l * modifier))
        k += 1
        modifier += p**k
    inset = newset.copy()
len(inset)
pset_fracs = {}
for s in tqdm(valid_psets):
    f = Fraction(1, 1)
    num = 1
    for p in s:
        num *= p
        f *= Fraction(p + 1, p)
    pset_fracs[f] = num
goods = set()
for e, ds in tqdm(inset):
    for tnum in range(3, 19, 2):
        tfrac = Fraction(tnum, 2)
        tcomp = tfrac / Fraction(ds, e)
        if tcomp in pset_fracs:
            num = pset_fracs[tcomp]
            goods.add(e * num)
            # print("FOUND", tnum, e * num)
goods = sorted(list(goods))
for e in goods:
    print(e, pfs(e))
# """
# FOUND 3 2
# FOUND 5 24
# FOUND 7 4320
# FOUND 7 4680
# FOUND 7 26208
# FOUND 7 57575890944
# FOUND 9 8910720
# FOUND 9 17428320
# FOUND 9 8583644160
# FOUND 7 20427264
# FOUND 7 301183421949935616
# FOUND 9 206166804480
# FOUND 9 1416963251404800
# FOUND 7 21857648640
# FOUND 5 10200236032
# FOUND 9 57629644800
# FOUND 11 17116004505600
# FOUND 9 200286975596707184640
# FOUND 11 59485231752222033838080
# FOUND 11 6219051710415667200
# FOUND 7 197064960
# FOUND 5 91963648
# FOUND 9 15338300494970880
# """
print(sum(e for e in goods if e <= N))