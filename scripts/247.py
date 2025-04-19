from heapq import *
from decimal import Decimal, getcontext
getcontext().prec = 32
def inter(x, y):
    X = ((x - y) + ((y - x)**Decimal(2) + Decimal(4))**Decimal(0.5)) / Decimal(2)
    Y = Decimal(1) / X
    return X, Y
def GAAP(x: Decimal, y: Decimal):
    upper = inter(x, y)
    area = (upper[1] - y) * (upper[0] - x)
    return (area, upper)
def fac(n):
    return 1 if n <= 1 else fac(n - 1) * n
def binom(n, k):
    return fac(n) // fac(n - k) // fac(k)
h = []
bp = (Decimal(1), Decimal(0))
area, upper = GAAP(*bp)
heappush(h, (-area, bp, upper, (0, 0)))
k = 3
OOC = binom(2 * k, k)
i = 0
while True:
    i += 1
    A, B, U, C = heappop(h)
    A = -A
    # print(i, A, float(B[0]), float(B[1]))
    if C == (k, k):
        OOC -= 1
        print("Seen", i)
    if OOC == 0:
        print("Done at", i)
        break
    pnts = [(U[0], B[1], 1, 0), (B[0], U[1], 0, 1)]
    for x, y, ld, rd in pnts:
        cc = (C[0] + ld, C[1] + rd)
        area, upper = GAAP(x, y)
        heappush(h, (-area, (x, y), upper, cc))
        
# 100: 782252