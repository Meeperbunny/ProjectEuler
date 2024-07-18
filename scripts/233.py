from math import gcd
from collections import Counter
maxn = 10**8
target = 420

print("Init count")
cnt = Counter()

prog = 120

m = 1
print("Starting Decomp")
while m * m < maxn:
    n = 1
    if m % (int(maxn**0.5) // prog + 1) == 0:
        a = m // (int(maxn**0.5) // prog + 1)
        print(a * "#" + (prog - a) * '.')
    while n < m and m * m + n * n < maxn:
        if (m + n) % 2 == 1 and gcd(m, n) == 1:
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
            inc = 2 * c * 10 // gcd(2 * c, 10)
            for q in range(inc, maxn + 1, inc):
                cnt[q] += 8
        n += 1
    m += 1
tot = 0

print("Adding all")
for i in cnt:
    if cnt[i] + 4 == target:
        tot += i
print("Answer:", tot)

# 1e4, 36 = 3059750
# 1e4, 36 = 1828070
# 1e7, 420 = 723294800
# 1e8, 420 = 110992152560
# 1e9, 420 = 12512869632780

# from math import gcd
# from collections import Counter
# maxn = 10**4
# target = 36

# fa = Counter()
# prog = 120

# def getfacs(n):
#     ret = []
#     for i in range(1, n + 1):
#         if n % i == 0:
#             ret.append(i)
#     return ret
# m = 1
# tot = 0
# while m * m <= maxn:
#     if m % (int(maxn**0.5) // prog + 1) == 0:
#         a = m // (int(maxn**0.5) // prog + 1)
#         print(a * "#" + (prog - a) * '.')
#     n = 1
#     while n < m and m * m + n * n <= maxn:
#         if (m + n) % 2 == 1 and gcd(m, n) == 1:
#             fa[m * m + n * n] += 1
#         n += 1
#     m += 1


# print(fa)
# # print(getfacs(10000))
# # tot = 0
# # for fac in getfacs(10000):
# #     tot += fa[fac] * 8
# # print(tot + 4)