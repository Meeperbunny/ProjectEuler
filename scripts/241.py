def divisors(n):
    t = 0
    for i in range(1, n + 1):
        if i * i == n:
            t += i
            return t
        if i * i > n:
            return t
        if n % i == 0:
            t += i + (n // i)
    return t

from fractions import Fraction
from tqdm import trange

gd = set()
for i in trange(1, 100_000_000):
    s = divisors(i)
    f = Fraction(i, s)
    if f.numerator % 2 == 1 and f.denominator == 2:
        print(i)
        gd.add(i)
print(gd)