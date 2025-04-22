def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

def binom(n, k):
    return factorial(n) // factorial(k) // factorial(n - k)