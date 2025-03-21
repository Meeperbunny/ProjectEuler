from math import gcd
N = 9000
ls = []
for p in range(1, N):
    for q in list(range(p, 2 * p)) + [p * (p - 1) + 1]:
        if gcd(p, q) == 1:
            # print(p, q, (p * q - 1) / (1 / p + 1 / q))
            upper = p * q * (p * q - 1)
            lower = p + q
            if upper % lower == 0:
                # print(p, q, q / p, upper // lower)
                # print(p * q - 1, p + q, "D", (p * q - 1) / (p + q))
                ls.append(upper // lower)
L = sorted(ls)
print(len(L), L[10_000])