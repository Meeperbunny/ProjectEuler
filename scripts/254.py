from utils.mckay import integer_partition
from utils.factorial import *
from itertools import permutations
from tqdm import tqdm
def getd(md):
    r = []
    b = [e for e in integer_partition(md) if len(e) <= 8]
    for e in tqdm(b):
        e = e + [0 for _ in range(8 - len(e))]
        r += list(set(permutations(e)))
    return r
def dsum(n):
    sn = str(n)
    return sum(ord(c) for c in sn) - len(sn) * ord('0')
msz = 5000
g = 150
mnum = -1
G = [mnum for _ in range(g + 1)]
G[0] = 0
for sz in range(1, 2 + 1):
    print("On size {}".format(sz))
    d = getd(sz)
    for e in tqdm(d):
        e = list(e + (0,))
        t = 0
        for i in range(1, 10):
            t += factorial(i) * e[i - 1]
        for q in range(msz):
            c = dsum(t)
            if c <= g:
                snum = 0
                for i in range(1, 10):
                    for q in range(e[i - 1]):
                        snum = snum * 10 + i
                if snum > 0:
                    if G[c] == -1:
                        G[c] = snum
                    G[c] = min(snum, G[c])
            t += factorial(9)
            e[-1] += 1
    print("UK", sum(e == -1 for e in G))
    print(sum(dsum(e) for e in G))
for i in range(g + 1):
    print(i, G[i])