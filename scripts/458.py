from utils.factorial import factorial
from utils.matrix import mult
fac = factorial(7)
# first is 0. second is either 0 or 1 if adding new. Then its 0 1 2 etc
def string_to_num(s):
    seen = {}
    cc = 1
    h = 0
    for c in s:
        if c not in seen:
            seen[c] = len(seen)
        h = h * cc + seen[c]
        cc += 1
    return h
base = [[0 for _ in range(fac)]]
transition = [[0 for _ in range(fac)] for _ in range(fac)]
seen = set()
for i in range(7**7):
    st = tuple((i//(7**q)) % 7 for q in range(7))
    code = string_to_num(st)
    if code != fac - 1:
        base[0][code] += 1
    if code in seen:
        continue
    seen.add(code)
    if code != fac - 1:
        # print(len(base), code)
        for new_end in range(0, 7):
            n_st = st[1:] + (new_end,)
            new_code = string_to_num(n_st)
            if new_code != fac - 1:
                transition[code][new_code] += 1
print(sum(base[0][i] for i in range(fac - 1)))

from tqdm import trange
def mult(A, B, mod=None):
    res = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    assert(len(A[0]) == len(B))
    for i in trange(len(A)):
        for j in range(len(B)):
            for q in range(len(B[0])):
                res[i][q] += A[i][j] * B[j][q]
                if mod:
                    res[i][q] %= mod
    return res

def matpow(m, k, mod=None):
    b = list(m)
    k -= 1
    while k:
        print(k)
        if k & 1:
            m = mult(b, m, mod)
            k -= 1
        else:
            b = mult(b, b, mod)
            k //= 2
    return m

mod = 10**9
N = 10**12
res = mult(base, matpow(transition, N - 7, mod=mod), mod=mod)
print(sum(res[0][i] for i in range(fac - 1)))