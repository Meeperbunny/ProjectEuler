import itertools

maxn = 52

def gen_primes(n):
    sieve = [1 for _ in range(n + 1)]
    primes = []
    for i in range(2, n + 1):
        if sieve[i]:
            primes.append(i)
            for q in range(2 * i, n + 1, i):
                sieve[q] = 0
    return primes

primes = gen_primes(maxn)
primes

def get_groups(p, n, plist):
    cands = list(range(p, n + 1, p))
    cands = [e for e in cands if e in plist]
    valid_cands = []
    for n_g in range(2, len(cands) + 1):
        for cand in itertools.combinations(cands, n_g):
            n, d = 0, 1
            for el in cand:
                n = d + el * el * n
                d = d * el * el
            if n % pow(p, 2 * len(cand)) == 0:
                # print(n, d, cand)
                valid_cands.append(cand)
    return valid_cands

g = {}
n_list = list(range(2, maxn + 1))

fnd = False

# for p in reversed(primes[1:]):
    # groups = get_groups(p, maxn, n_list)
    # g[p] = groups
    # opr = False
    # if not len(groups) and not fnd:
    #     opr = True
    #     for el in range(p, maxn + 1, p):
    #         if el in n_list:
    #             n_list.remove(el)
    # else:
    #     opr = False
    #     fnd = True
    # print(p, len(groups), opr)
    # if p * 3 > maxn:
    #     print(p * 3)
    #     for el in range(p, maxn + 1, p):
    #         if el in n_list:
    #             print(el)
    #             n_list.remove(el)

from math import lcm
from collections import Counter

print(n_list)

l_a = 1
for e in n_list:
    l_a = lcm(l_a, e * e)
print(l_a)
tar = l_a // 2

n_list_f, n_list_s = n_list[:len(n_list)//2], n_list[len(n_list)//2:]
print(n_list_f, n_list_s)

ways_f, ways_s = Counter(), Counter()
ways_f[0], ways_s[0] = 1, 1

for i, e in enumerate(n_list_f):
    print(i, e, len(n_list_f))
    for b_v in ways_f.copy():
        cnt = ways_f[b_v]
        t_a = l_a // (e * e)
        if (b_v + t_a <= tar):
            ways_f[b_v + t_a] += cnt
for i, e in enumerate(n_list_s):
    print(i, e, len(n_list_s))
    for b_v in ways_s.copy():
        cnt = ways_s[b_v]
        t_a = l_a // (e * e)
        if (b_v + t_a <= tar):
            ways_s[b_v + t_a] += cnt
print("MEETING")
# MEET IN THE MIDDLE
tot = 0
for e in ways_f:
    cnt_f = ways_f[e]
    t_s = tar - e
    cnt_s = ways_s[t_s]
    tot += cnt_f * cnt_s
print("Answer:", tot)