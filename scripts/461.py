
from decimal import Decimal, getcontext
from math import pi, exp
from tqdm import tqdm
from bisect import *

n = 10_000
PI = pi

l = [(exp(k / n) - 1, k * k) for k in range(1, int(n * 1.2))]

comb = []
print("adding")
for i, a in tqdm(enumerate(l)):
    comb += [(a[0] + b[0], a[1] + b[1]) for b in l[i:]]
print("sortiung")
comb.sort()

best_error = PI
best_indices = None

print("iterating")

for e in tqdm(comb):
    comp = PI - e[0]
    k = -1
    j = len(comb)
    while j >= 1:
        while True:
            nk = k + j
            if nk >= len(comb):
                break
            if comb[nk][0] > comp:
                break
            k = nk
        j //= 2
    if k >= 0:
        er = abs(e[0] + comb[k][0] - PI)
        if er < best_error:
            best_error = er
            best_indices = e[1] + comb[k][1]
    if k + 1 < len(comb):
        er = abs(e[0] + comb[k + 1][0] - PI)
        if er < best_error:
            best_error = er
            best_indices = e[1] + comb[k + 1][1]


print(best_indices, best_error)
t = 0
for i in best_indices:
    t += i * i
print(t)





