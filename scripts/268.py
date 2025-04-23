from tqdm import trange, tqdm
from itertools import combinations
from math import log

def sieve(n):
    s = [1 for _ in range(n + 1)]
    primes = []
    for q in range(2, n + 1):
        if s[q]:
            primes.append(q)
            for i in range(2 * q, n + 1, q):
                s[i] = 0
    return primes
primes = sieve(100)
N = 10**16
def populate(t):
    tt = 0
    global N
    c = 1
    for e in t:
        c *= e
    cnts = [1 for _ in t]
    if c < N:
        tt += 1
    while True:
        cnts[0] += 1
        c *= t[0]
        for i in range(len(t)):
            if c > N:
                if i == len(t) - 1:
                    return tt
                c //= t[i]**(cnts[i] - 1)
                c *= t[i + 1]
                cnts[i] = 1
                cnts[i + 1] += 1
        if c < N:
            tt += 1
s = set()
T = 0
for sz in range(4, 25):
    print(sz)
    for c in combinations(primes, sz):
        T += populate(c)
    print(T)
print("ANSWER", T)

# from tqdm import trange, tqdm
# from itertools import combinations
# from math import log

# def sieve(n):
#     s = [1 for _ in range(n + 1)]
#     primes = []
#     for q in range(2, n + 1):
#         if s[q]:
#             primes.append(q)
#             for i in range(2 * q, n + 1, q):
#                 s[i] = 0
#     return primes
# from sortedcontainers import SortedSet
# pind = {}
# primes = sieve(100)
# for i in range(len(primes)):
#     pind[primes[i]] = i
# N = 10**16
# lks = {0: {0: SortedSet({1})}}
# for sz in trange(1, 13):
#     lks[sz] = {}
#     for p in tqdm(primes):
#         pi = pind[p]
#         for key in lks[sz - 1]:
#             if (key >> pi) & 1:
#                 continue
#             masked = key | (1 << pi)
#             if masked not in lks[sz]:
#                 lks[sz][masked] = SortedSet()
#             for k in range(1, 100):
#                 bnum = p**k
#                 for el in lks[sz - 1]:
#                     nn = bnum * el
#                     if nn > N:
#                         break
#                     lks[sz][masked].add(nn)
# T = 0
# for k, v in lks.items():
#     for e in v:
#         if k >= 4:
#             T += len(e)
#     # print(k, v)
# print(T)
                
        
"""
4
100%|███████████████████████████████████████████████████████████████████████████████| 12650/12650 [00:01<00:00, 12199.27it/s]
8373166
5
100%|████████████████████████████████████████████████████████████████████████████████| 53130/53130 [00:07<00:00, 6671.06it/s]
66344729
6
100%|███████████████████████████████████████████████████████████████████████████████| 177100/177100 [06:50<00:00, 431.88it/s]
293860638
"""