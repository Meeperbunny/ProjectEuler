from math import log2

n = 10000000
m = 10000000
mod = int(1e9 + 7)
nimber_size = int(log2(n) + 1)
n, nimber_size

from collections import Counter

nimbers = [Counter() for _ in range(nimber_size)]
nimbers[0][1] = 1

print("Sieving")

s = [1 for _ in range(n)]
nimber = 1
for q in range(2, n):
    if s[q]:
        for i in range(q, n, q):
            if s[i]:
                if q == 2:
                    # print(i, 0)
                    nimbers[0][0] += 1
                else:
                    # print(i, nimber)
                    nimbers[0][nimber] += 1
            s[i] = 0
        nimber += 1

print("Splitting")

for i in range(1, nimber_size):
    for ind, e in enumerate(nimbers[i - 1]):
        if ind % (len(nimbers[i - 1]) // 10000) == 0:
            print(ind / len(nimbers[i - 1]) / nimber_size)
        for q in nimbers[i - 1]:
            nimbers[i][e ^ q] = (nimbers[i][e ^ q] + nimbers[i - 1][e] * nimbers[i - 1][q]) % mod

print("Decomposing")

base = Counter([0])
left = m
for i in range(nimber_size - 1, -1, -1):
    take = 1 << i
    while take <= left:
        left -= take
        print("Taking", take)
        new_base = Counter()
        for e in base:
            for q in nimbers[i]:
                new_base[e ^ q] = (new_base[e ^ q] + base[e] * nimbers[i][q]) % mod
        base = new_base
print(base[0] % mod)