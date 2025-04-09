
def get_divs(n):
    divs = [[] for _ in range(n + 1)]
    for i in trange(1, n + 1):
        for q in range(i, n + 1, i):
            divs[q].append(i)
    return divs

def combine_divs(A, B):
    d = set()
    for d1 in A:
        for d2 in B:
            if d1 & 1 and d2 & 1:
                pass
            else:
                d.add(d1 * d2)
    return list(d)
from tqdm import trange
N = 25_000_000
D = get_divs(N // 3 + 2)
C = (N - 1) // 2
for k in trange(1, N // 3 + 1):
    A = D[k - 1]
    B = D[k + 1]
    comb = combine_divs(A, B)
    for d in comb:
        if d % 2 == 0:
            j = d // 2
            i = (k**2 - 1) // (2 * j) - j
            rt = round((2 * j**2 + 2 * i * j + 1)**0.5)
            a_u = j + rt
            b_u = a_u + i
            c_u = a_u + i + j
            if a_u >= 1 and a_u <= b_u and a_u + b_u + c_u <= N:
                C += 1
print(C)