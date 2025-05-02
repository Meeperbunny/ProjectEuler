def to_base(n, k):
    t = []
    while n:
        t.append(n % k)
        n //= k
    return tuple(t)
def to_num(t, b):
    n = 0
    for e in t:
        n = n * b + e
    return n
from itertools import permutations
def is_pandigital(t, b):
    cnts = [0 for _ in range(b)]
    for e in t:
        cnts[e] += 1
    return min(cnts) != 0
from tqdm import tqdm
sz = 12
C = 10
T = 0
tp = tuple(i for i in range(sz))
ps = permutations(tp)
for perm in ps:
    if perm[0] == 0:
        continue
    num = to_num(perm, sz)
    w = True
    for b in range(2, sz + 1):
        t = to_base(num, b)
        if not is_pandigital(t, b):
            w = False
            break
    if w:
        print("Found one!")
        C -= 1
        T += num
        if C == 0:
            break
print(T)