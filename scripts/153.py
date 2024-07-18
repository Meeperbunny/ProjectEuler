from math import gcd
def divsum(n):
    maxn = int(n)
    max_sq = int(maxn**0.5)
    mod = int(1e9)
    # def sq_sum(n):
    #     return n * (n + 1) * (2 * n + 1) // 6
    def norm_sum(n):
        return n * (n + 1) // 2
    tot = 0
    for i in range(1, max_sq + 1):
    #     if i % (max_sq // 10) == 0:
    #         a = i // (max_sq // 10)
    #         print("#" * a + '.' * (10 - a))
        # Definer lower part
        cnt = maxn // i
        lower = (maxn // i - i + 1) * (i)
        # Define upper part
    #     print(cnt, i, sq_sum(cnt), sq_sum(i))
        upper = (norm_sum(cnt) - norm_sum(i))
    #     print(i, lower, upper)
        tot += lower + upper
        tot %= mod
    return tot

def ans(n):
    seen = set()
    g = 1
    tot = [0 for _ in range(n + 1)]
    while g <= n:
        if g < 1000:
            print(g)
        if g % 10000 == 0:
            print(g / n)
        a = g
        while a * a  <= n * g:
            b = g
            while a * a + b * b <= n * g:
                imp_d = (a * a + b * b) // g
                # new_g = gcd(a, b)
                # if new_g * new_g > n or new_g == g:
                    # print(a, b, imp_d, (n) // imp_d * 2 * a)
                    # tot[0] += (n) // imp_d * 2 * a
                for imp_n in range(imp_d, n + 1, imp_d):
                    # if (a, b, imp_n) not in seen:
#                         print('\t', a, b, imp_n)
                        tot[imp_n] += 2 * a
                        # seen.add((a, b, imp_n))
                b += g
            a += g
        g += 1
    return sum(tot)
n = 100000
res = ans(n) + divsum(n)
print("Answer:", res)
# assert(res == 1304302582)
# print("Is Good")
