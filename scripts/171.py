#!/usr/bin/env pypy
from collections import Counter

def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1

def solve(max_digits):
#     max_digits = 20
    maxn = 10**max_digits

    max_sq = int((9**2 * (max_digits + 1))**0.5)**2

    can_reach = [[False for _ in range(max_sq + 1)] for _ in range(max_digits + 1)]
    can_reach[0][0] = True

    print("[PROGRESS] Finding Reachable Squares...")
    for d in range(1, 10):
        d_add = d * d
        for n in range(max_digits):
            for i in range(max_sq):
                if can_reach[n][i]:
                    if i + d_add <= max_sq:
                        can_reach[n + 1][i + d_add] = True

    reachable_squares = set()

    i = 1
    while i * i <= max_sq:
        for q in range(max_digits + 1):
            if can_reach[q][i * i]:
                reachable_squares.add(i * i)
        i += 1
    print("[PROGRESS] Done.")

    def decomp(n, rlist, last=9, left=max_digits, cc = Counter()):
        if last == 0:
            if n == 0:
                rlist.append(cc.copy())
            return
        for used in range(0, left + 1):
            if last * last * used > n:
                break
            if used:
                cc[last] += used
            decomp(n - last * last * used, rlist, last - 1, left - used, cc)
            if used:
                cc[last] -= used

    # Find the counts for each squre decomp
    sq_decomps = []
    for sq in reachable_squares:
        print("[PROGRESS] Decomposing", sq)
        decomp(sq, sq_decomps)

    ans = 0
    mod = 1000000000

    num, den = factorial(max_digits - 1), 1
    tc = Counter()
    for cnt in sq_decomps:
        new_cnt = Counter()
        tot_nums = 0
        for e in cnt:
            if cnt[e] != 0:
                tot_nums += cnt[e]
                new_cnt[e] = cnt[e]
        new_cnt[0] = max_digits - tot_nums
#         print(new_cnt)

        b_num, b_den = int(num), int(den)
    #     print(base_fac, base_mult, new_cnt)
        for el in new_cnt:
#             print(factorial(new_cnt[el]))
            b_den *= int(factorial(new_cnt[el]))

        for digit in new_cnt:
            for place in range(0, max_digits):
                pl_m = 10**place
                times = int((b_num * new_cnt[digit]) / b_den)
                tc[pl_m * digit] += times
                ans = (ans + pl_m * digit * times) % mod
    return ans
print(solve(20))