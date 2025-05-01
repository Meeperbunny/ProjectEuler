from functools import cache

@cache
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

@cache
def binom(n, k):
    return factorial(n) // factorial(k) // factorial(n - k)

@cache
def multi(t):
    s = sum(t)
    b = 1
    for e in t:
        b *= factorial(e)
    return factorial(s) // b