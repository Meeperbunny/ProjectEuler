from utils.sieve import *
primes = [e for e in sieve(150) if (e - 1) % 4 == 0]
primes
to_check = []
for i in range(1, 2**len(primes)):
    m = 1
    for q in range(len(primes)):
        if (i >> q) & 1:
            m *= primes[q]
    to_check.append(m)
len(to_check), to_check[0:10]
def get_square(n):
    l = int(n**0.5)
    if l * l == n:
        return l
    if (l + 1) * (l + 1) == n:
        return l + 1
    return -1
def S(n):
    T = 0
    for a in range(1, n // 2 + 1):
        asq = a**2
        diff = n - asq
        if asq > n // 2:
            break
        # print(a, n, diff)
        if diff <= 0:
            break
        b = get_square(diff)
        if b == -1:
            continue
        if b < a:
            break
        if b != -1:
            T += a
    return T

from tqdm import tqdm
T = 0
for e in tqdm(to_check):
    T += S(e)
print(T)