def cyclic_shift(t):
    return list((tuple(t[(i + q) % len(t)] for q in range(len(t)))) for i in range(len(t)))
# cyclic_shift((1, 2, 3, 4, 5))
from collections import Counter
from tqdm import trange
def f(m, n):
    n = m * n
    c = 0
    gs = set()
    for i in trange(pow(m, n)):
        cs = tuple(i // m**(q) % m for q in range(n))
        ccs = cyclic_shift(cs)
        cnt = Counter(cs)
        if min(cnt.values()) == max(cnt.values()) and len(cnt) == m:
            if all(e not in gs for e in ccs):
                # print(cs)
                gs |= set(ccs)
                c += 1
    return c
print(f(3, 5))