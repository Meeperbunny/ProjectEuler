from math import lcm
from fractions import Fraction
s = [2, 3, 4, 5, 7, 12, 15, 20, 28, 35]
def pfs(n):
    pfs = []
    for i in range(2, n):
        if i * i > n:
            break
        while n % i == 0:
            n //= i
            pfs.append(i)
    if n - 1:
        pfs.append(n)
    return pfs
def get_lpf(i):
    ps = set(pfs(i))
    return max(ps)
def get_spf(i):
    ps = set(pfs(i))
    return min(ps)
s = [2, 3, 4, 6, 7, 9, 12, 15, 28, 30, 35, 36, 45]
s = [2, 3, 4, 6, 7, 9, 10, 20, 28, 35, 36, 45]
from fractions import Fraction
N = 80
# t = 27
# N = 45
t = 25
s = [i for i in range(3, N + 1)]
c = {}
for e in s:
    # lp = get_spf(e)
    # lp = get_lpf(e)
    if lp not in c:
        c[lp] = []
    c[lp].append(e)
T = Fraction(0)
for e, v in c.items():
    f = Fraction(0)
    for i in v:
        f += Fraction(1, i * i)
    print(e, v, f)
    T += f
T
nums = []
for e, v in c.items():
    for k in v:
        if get_spf(k) <= 13:
            nums.append(Fraction(1, k * k))
lc = 1
for i in nums:
    lc = lcm(lc, i.denominator)

for i in range(len(nums)):
    nums[i] = lc * nums[i].numerator // nums[i].denominator

l1 = nums[:t]
l2 = nums[t:]


f = Fraction(0)
for k in [13, 39, 52]:
    f += Fraction(1, k * k)
print(f, f * lc)

print(lc)
print(l1, l2)
from tqdm import tqdm
def gen_cset(l, lc):
    s = [0]
    for q, n in enumerate(l):
        print(q)
        ssz = len(s)
        for i in tqdm(range(ssz)):
            if s[i] + n > lc // 2:
                continue
            s.append(s[i] + n)
    return s
def fac(n):
    return 1 if n <= 1 else fac(n - 1) * n
def binom(n, k):
    return fac(n) // fac(n - k) // fac(k)
from collections import Counter
print("GENERATING")
ss = None
ss = Counter(gen_cset(l1, lc))
# print(len(ss) / pow(2, len(l1)))
c = 0
tar = lc // 2 - lc // 4
from itertools import combinations
for sz in range(13, len(l2) + 1):
    # print("checking sz", sz)
    # for combo in tqdm(combinations(l2, r=sz)):
    b = binom(len(l2), sz)
    gen = combinations(l2, r=sz)
    for _ in tqdm(range(b)):
        combo = next(gen)
        comp = tar - sum(combo)
        if comp in ss:
            tt = Counter()
            for e in combo:
                q = int((lc // e)**0.5)
                tt[get_lpf(q)] += 1
                print(q, end=", ")
            print()
            print(tt)
            print()
            c += ss[comp]
            print(c)
print(c)
    # break

"""
33it [00:00, ?it/s]
0
checking sz 2
528it [00:00, 263956.20it/s]
0
checking sz 3
5456it [00:00, 79418.50it/s]
49
checking sz 4
40920it [00:00, 2341358.18it/s]
70
checking sz 5
237336it [00:00, 2176885.66it/s]
81
checking sz 6
1107568it [00:00, 2417723.55it/s]
195
checking sz 7
4272048it [00:01, 2489952.45it/s]
213
checking sz 8
13884156it [00:05, 2453990.65it/s]
225
checking sz 9
38567100it [00:16, 2373347.50it/s]
288
checking sz 10
92561040it [00:41, 2248275.96it/s]
288
checking sz 11
193536720it [01:27, 2218552.97it/s]
288
checking sz 12
354817320it [02:44, 2156349.99it/s]
296
checking sz 13
573166440it [04:30, 2116452.72it/s]
296
checking sz 14
818809200it [06:46, 2014030.15it/s]
296
checking sz 15
1037158320it [08:40, 1994339.26it/s]
296
checking sz 16
"""