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
    return tot
n = int(1e8)
t = 0
for g in range(1, n + 1):
    if g < 1000:
        print(g)
    if g % (n // 100) == 0:
        cn = (g // (n // 100))
        print("#" * cn + "." * (100 - cn))
    for a in range(g, n + 1, g):
        for b in range(g, n + 1, g):
            if (a * a + b * b) // g > n:
                break
            gp = gcd(a, b)
            if g == gp:
                nu = (a*a+b*b) // g
                t += (n // nu) * a * 2
print(t, t + divsum(n))