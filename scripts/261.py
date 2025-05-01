from tqdm import trange

from collections import Counter
cc = Counter()

def get_square(n):
    l = int(n**0.5)
    if l * l == n:
        return l
    if (l + 1) * (l + 1) == n:
        return l + 1
    return -1

s = set()
N = 3 * 10**7
K = 24

m = 1
while True:
    n = 2 * m + 2 * m**2
    if n > N:
        break
    # s.add(n)
    m += 1

mm = 0
for n in trange(1, N + 1):
    for m in {8, 24, 48, 49, 80, 120, 168, 242, 288}:
    # for m in range(1, min(n + 1, K + 1)):
        if n == 2 * m + 2 * m**2:
            continue
        a, b, c = -m, -m**2 - 2*m*n + m, - 2*m**2*n + m**2 + n**2
        inner = b**2 - 4 * a * c
        sq = get_square(inner)
        if sq != -1:
            e = -b - sq
            if e % (2 * a) == 0:
                k = e // (2 * a)
                if k > 0:
                    # if n not in S:
                    #     print("NOT IN", n, m, k)
                    # print(n, m, k)
                    s.add((n, m, k))
                    cc[k] += 1
                    mm = max(m, mm)
# print(sum(s), cc, cc.values(), mm)
# print(sum(s))
print(s)