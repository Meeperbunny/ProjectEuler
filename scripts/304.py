#!/usr/bin/env pypy
import numpy as np
from numpy import asanyarray, issubdtype, binary_repr, dot, identity

from random import randint
def miller_rabin(n, k=40):
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

m_ta = {}
def matrix_mod_exp(A, P, M):
    def matrix_mult_mod(A, B, M):
        # Perform element-wise multiplication followed by modulo operation
        return np.remainder(np.dot(A, B) % M, M)

    def matrix_pow_mod(A, P, M):
        global m_ta
        if P not in m_ta:
            # Initialize the result as the identity matrix
            result = np.eye(A.shape[0], dtype=object)
            base = A.copy()

            while P > 0:
                if P % 2 == 1:
                    result = matrix_mult_mod(result, base, M)
                base = matrix_mult_mod(base, base, M)
                P //= 2
            m_ta[P] = result
            
        return m_ta[P]

    return matrix_pow_mod(A, P, M)

def fib(n, mod):
    a = np.matrix([
        [1, 1],
        [1, 0],
    ], dtype=object)
    return matrix_mod_exp(a, n - 1, mod)[0, 0]

c_n = 10**14
pc = 100_000
mod = 1234567891011
a = []
while len(a) < pc:
    if miller_rabin(c_n):
        if len(a) % (pc // 100) == 0:
            prog = len(a) // (pc // 100)
            print("#" * prog + '.' * (100 - prog))
        a.append(c_n)
    c_n += 1

print("Calculating Total")
tot = 0
for i, n in enumerate(a):
    if i % (pc // 100) == 0:
        prog = i // (pc // 100)
        print("#" * prog + '.' * (100 - prog))
    tot += fib(n, mod)

print(tot % mod)