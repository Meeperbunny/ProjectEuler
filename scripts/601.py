from math import gcd

def s(n, s):
    for i in range(s):
        if (n + i) % (i + 1) != 0:
            return False
    return ((n + s) % (s + 1) != 0)

def lcm_fac(k):
    b = 1
    for i in range(2, k + 1):
        b = (b * i) // gcd(b, i)
    return b

cnt = 0
for i in range(1, 31 + 1):
    print(f"[FINISHED WITH i = {i}]")
    mult = lcm_fac(i)
    ub = pow(4, i)
    for q in range(mult + 1, ub, mult):
        if s(q, i):
            cnt += 1
print(cnt)
input()