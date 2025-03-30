from fractions import Fraction
from decimal import Decimal, getcontext

getcontext().prec = 200

class SternBrocot:
    def __init__(self, max_den_sum):
        self.max_den_sum = max_den_sum

    def traverse(self, t: Fraction):
        t_decimal = Decimal(t.numerator) / Decimal(t.denominator)
        sqrt_t = t_decimal.sqrt()
        
        self.min_diff = Decimal('Infinity')
        self.best_frac = (0, 1)
        self.l = (0, 1)
        self.m = (1, 1)
        self.r = (1, 0)

        def iter_step():
            m_value = Decimal(self.m[0]) / Decimal(self.m[1])
            diff = abs(m_value - sqrt_t)
            if diff < self.min_diff:
                self.min_diff = diff
                self.best_frac = self.m
            m_squared = m_value * m_value
            if m_squared < t_decimal:
                self.l = self.m
                if self.l[1] + self.r[1] > self.max_den_sum:
                    return True
                self.m = (self.l[0] + self.r[0], self.l[1] + self.r[1])
            else:
                self.r = self.m
                if self.l[1] + self.r[1] > self.max_den_sum:
                    return True
                self.m = (self.l[0] + self.r[0], self.l[1] + self.r[1])
            return False
        while True:
            if iter_step():
                return self.best_frac

stern = SternBrocot(10**12)
squares = {i * i for i in range(1, 10000)}
T = 0
from tqdm import trange
for i in trange(2, 100_000 + 1):
    if i not in squares:
        best_fraction = stern.traverse(Fraction(i))
        T += best_fraction[1]

print("Total sum:", T)
