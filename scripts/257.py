
from tqdm import trange

def get_divs(n):
    divs = [[1] for _ in range(n + 1)]
    for i in trange(2, n + 1):
        for q in range(i, n + 1, i):
            divs[q].append(i)
    return divs

def combine_divs(d1, d2):
    dset = set()
    for a in d1:
        for b in d2:
            dset.add(a * b)
    return list(dset)

N = 10**6
# D = get_divs(N // 3 + 1)
T = 0

# K = 3
s = set()

for i in trange(1, N // 3 + 1):
    s.add((i, i, i))

from sympy import divisors
for a in trange(1, N // 3 + 1):
    D = divisors(a)
    for m in {1, 2}:
        for d1 in D:
            if d1 * 1 * m + a + a > N:
                break
            for d2 in D:
                if d1 * d2 * m + a + a > N:
                    break
                i = d1 * d2 * m
                j = (2 * a**2) // i
                if i <= j:
                    b = a + i
                    c = a + j
                    if a + b + c <= N:
                        if a <= b <= c and a + b + c <= N and not (a + b <= c):
                            if b*c == a * (a+b+c):
                                s.add((a, b, c))
                                T += 1
    for m in {1, 3}:
        for d1 in D:
            if (d1 * 1 * m - a) // 2 + a > N:
                break
            for d2 in D:
                if (d1 * d2 * m - a) // 2 + a > N:
                    break
                d = d1 * d2 * m
                o = (3 * a**2) // d
                i = (d - a) // 2
                j = (o - a) // 2
                if i <= j:
                    b = a + i
                    c = a + j
                    if a + b + c <= N:
                        if a <= b <= c and a + b + c <= N and not (a + b <= c):
                            if 2*b*c == a * (a+b+c):
                                s.add((a, b, c))
                                T += 1
print(len(s))
            