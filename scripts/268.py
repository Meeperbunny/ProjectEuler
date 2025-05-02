N = 10**6
from sympy import primepi as pi
# from utils.pi import pi
from utils.sieve import *
primes = sieve(100)
from tqdm import tqdm
from sympy import primefactors
cnts = [0 for _ in range(4)]
for i in range(1, 1000 + 1):
    pfs = set(primefactors(i))
    s = sum(p in primes for p in pfs)
    # if 2 in pfs and 3 in pfs and s == 2 and len(pfs) > 2 and (i // 2) & 1 and (i // 3) % 3:
    #     print(i)
    if s < 4:
        cnts[s] += 1
cnts, [sum(cnts[:i]) for i in range(1, 4 + 1)]
from math import log
T = 1
# No primes
T += pi(N) - pi(100)
print(T)
# One prime
def gr(p):
    return int(log(N, p) + 1)
for i, p1 in tqdm(enumerate(primes)):
    for k1 in range(1, gr(p1)):
        num = p1**k1
        kk = N // num
        if kk == 0:
            break
        if kk < 100:
            T += 1
        else:
            # print(num, kk, pi(min(N, kk)) - pi(100))
            T += 1 + pi(min(N, kk)) - pi(100)
print(T)
# Two primes
for i, p1 in tqdm(enumerate(primes)):
    for q, p2 in enumerate(primes[i+1:]):
        for k1 in range(1, gr(p1)):
            for k2 in range(1, gr(p2)):
                num = p1**k1 * p2**k2
                kk = N // num
                if kk == 0:
                    break
                if kk < 100:
                    T += 1
                else:
                    # print(num, kk, 1 + pi(min(N, kk)) - pi(100))
                    T += 1 + pi(min(N, kk)) - pi(100)
print(T)
# Three primes
for i, p1 in tqdm(enumerate(primes)):
    for q, p2 in enumerate(primes[i+1:]):
        for j, p3 in enumerate(primes[i+1+q+1:]):
            for k1 in range(1, gr(p1)):
                for k2 in range(1, gr(p2)):
                    for k3 in range(1, gr(p3)):
                        num = p1**k1 * p2**k2 * p3**k3
                        kk = N // num
                        if kk == 0:
                            break
                        if kk < 100:
                            T += 1
                        else:
                            # print(num, kk, pi(min(N, kk)) - pi(100))
                            T += 1 + pi(min(N, kk)) - pi(100)
print(N - T)