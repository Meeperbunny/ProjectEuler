from tqdm import trange
from sympy import factorint
def prime_factors(n: int):
    return [p for p, e in factorint(n).items() for _ in range(e)]

def get_pfs(n):
    pfs = [[] for _ in range(n + 1)]
    for i in trange(2, n + 1):
        if len(pfs[i]) == 0:
            k = 1
            while i**k <= n:
                inc = i**k
                for q in range(inc, n + 1, inc):
                    pfs[q].append(i)
                k += 1
    return pfs
N = 110000000
# P = get_pfs(int(N * 8 / 3 + 10))
C = 0
msz = 0
asz = 0
ss = set()
for a in trange(2, N + 1, 3):
    b = (a + 1) // 3
    c = b * 8 - 3
    sqpfs = prime_factors(b)
    i = 0
    pc = prime_factors(c)
    while i < len(pc) - 1:
        if pc[i] == pc[i + 1]:
            sqpfs.append(pc[i])
            i += 1
        i += 1
    s = set({1})
    for e in sqpfs:
        cc = set()
        for el in s:
            cc.add(e * el)
        s.update(cc)
    bbc = b * b * c
    for pb in s:
        pc = bbc // (pb * pb)
        if a + pb + pc <= N:
            C += 1
print(N, c)
print(C)