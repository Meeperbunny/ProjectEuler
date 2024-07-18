#!/usr/bin/env pypy

maxn = 2022
mod = 1_000_000_007

m_factorial = {}
def factorial(n):
    global m_factorial
    if n not in m_factorial:
        m_factorial[n] = (n * factorial(n - 1)) % mod if n > 1 else 1
    return m_factorial[n]

m_binomial = {}
def binomial(n, k):
    global m_binomial
    if (n, k) not in m_binomial:
        m_binomial[(n, k)] = (factorial(n) * pow(factorial(k) * factorial(n - k), -1, mod)) % mod
    return m_binomial[(n, k)]

def s(N, c, d):
    if N == c:
        if d == 0:
            return 0
        else:
            return 1
    if d == 0:
        return (binomial(N - 1, c) * pow(9, N - c, mod)) % mod
    tot = (binomial(N - 1, c) * 8 * pow(9, N - c - 1, mod)) % mod
    tot = (tot + binomial(N - 1, c - 1) * pow(9, N - c, mod)) % mod
    return tot

def d(N, c):
    tot = 0
    for d in range(0, 10):
#         print(d, c, N, s(N, c, d))
        tot = (tot + s(N, c, d)) % mod
    return tot

def D(N):
    tot = 0
    for c in range(N // 2 + 1, N + 1):
#         print(c, d(N, c))
        tot = (tot + d(N, c)) % mod
    return tot

def S(N):
    tot = 0
    for i in range(1, N + 1):
        print(f"On i = {i}")
        tot = (D(i) + tot) % mod
    return tot

print(S(maxn))