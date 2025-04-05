from math import gcd
from collections import Counter
from tqdm import trange
4 * 7 - 2
def pfs(n):
    pfs = []
    for i in range(2, n + 1):
        while n % i == 0:
            n //= i
            pfs.append(i)
    return pfs
N = 50_000
ls = set()
for p in trange(2, N):
    for q in list(range(p, 2 * p)): # [p * (p - 1) + 1]:
        if gcd(q, p) != 1:
            continue
        upper = p * q * (p * q - 1)
        lower = p + q
        if upper % lower == 0:
            num = upper // lower
            r = num // (p * q)
            ls.add(num)
print(len(ls), len(set(ls)))
L = sorted(list(ls))
# print("ANSWER:", L[150_000 - 1])
print(len(L))
# L
# 10_000 -> 11929, 9994001399850006 (WITH N+1)
# 20_000 -> 3879, 10333415040954 (Without)
# 50_000 -> 9713, 163794346028280
# 50_000 -> ANS: 18988538300424



# from math import gcd
# from collections import Counter
# from tqdm import trange
# 4 * 7 - 2
# def pfs(n):
#     pfs = []
#     for i in range(2, n + 1):
#         while n % i == 0:
#             n //= i
#             pfs.append(i)
#     return pfs
# N = 100
# ls = []
# for p in trange(2, N):
#     for q in list(range(p, 2 * p)):#+ [p * (p - 1) + 1]:
#         if True:
#             # print(p, q, (p * q - 1) / (1 / p + 1 / q))
#             upper = p * q * (p * q - 1)
#             lower = p + q
#             if upper % lower == 0:
#                 num = upper // lower
#                 r = num // (p * q)
#                 # print("## PQR:", "({}, {}, {})".format(p, q, r), num)
#                 # print((p * q - 1), (p + q), (1 - p * q)/(p + q))
#                 # print()
#                 if gcd(p, q) != 1:
#                     print("AAA", (num, p, q, r), r * q)
#                 ls.append(num)
#                 # print(p, q)
# L = sorted(ls)
# print(len(L), len(set(L)))
# print(len(L), max(L))
# # L
# # 10_000 -> 11929, 9994001399850006 (WITH N+1)
# # 20_000 -> 3879, 10333415040954 (Without)
# # 50_000 -> 9713, 163794346028280