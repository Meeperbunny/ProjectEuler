from math import log2
from tqdm import *
mnum = 10000
bits = int(log2(mnum) + 2)
isprime = [[] for _ in range(mnum + 1)]
for i in tqdm(range(2, mnum)):
    for q in range(2, mnum):
        ans = 0
        for j in range(bits):
            if (i >> j) & 1:
               ans ^= (q << j)
        if ans <= mnum:
            isprime[ans].append((i, q))
primes = [(i, isprime[i]) for i in range(2, mnum + 1) if len(isprime[i])]
for p in primes:
    f = len(bin(p[1][0][0])+bin(p[1][0][1]))
    has_full = False
    for e in p[1]:
        l = len(bin(e[0])+bin(e[1]))
        if l != f:
            assert(False)
        if len(bin(e[1])) - 2 == sum([c == '1' for c in bin(e[1])]):
            has_full = True
    if not has_full:
        print(p)
        print(bin(p[0]))
        for e in p[1]:
            print(e[0], e[1], bin(e[0]), bin(e[1]))
print(len(primes))
