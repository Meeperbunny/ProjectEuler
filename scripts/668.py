def pi(n):
    r = int(n ** 0.5)
    assert r * r <= n and (r + 1) ** 2 > n
    V = [n // i for i in range(1, r + 1)]
    V += list(range(V[-1] - 1, 0, -1))
    D = {v: v - 1 for v in V}
    for p in range(2, r + 1):
        if D[p] > D[p - 1]:  # this indicates that p is prime
            # For each v in V with v >= p*p, update D[v]
            for v in V:
                if v < p * p:
                    break
                D[v] -= D[v // p] - D[p - 1]
    return D[n]

from tqdm import tqdm
from random import randint
def miller_rabin(n, k=5):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    
    y = 0
    for _ in range(k):
        a = randint(2, n - 2)
        x = pow(a, d, n)
        for _ in range(s):
            y = pow(x, 2, n)
            if y == 1 and x != 1 and x != n - 1:
                return False
            x = y
        if y != 1:
            return False
    return True

def ans_f(n):
    cnt = 0
    lta = 0
    for i in range(2, n + 1):
        if (miller_rabin(i)):
            max_val = min(n, i * i)
            min_val = i
            ta = (max_val) // i
            # print(i, ta)
            if ta < lta:
                break
            cnt += ta
            lta = ta
    # print(cnt)
    for i in tqdm(range(lta - 1, 0, -1)):
        # Find num of sols for i]
        p_l = (n + i) // (i + 1)
        p_r = n // i
        primes_inside = pi(p_r) - pi(p_l - 1)
        cnt += i * primes_inside
        # print(i,  p_r, p_l, pi(p_r), pi(p_l - 1), primes_inside, lta, lta * primes_inside)
    return n - cnt

n = 10**10
print(ans_f(n))