def totient(n):
    tot = [1 for i in range(n + 1)]
    for p in range(2, n + 1):
        if tot[p] == 1:
            # is prime
            k = 1
            while True:
                b = p**k
                if b > n:
                    break
                j = p
                if k == 1:
                    j = p - 1
                for q in range(b, n + 1, b):
                    tot[q] *= j
                k += 1
    return tot

def geo(n, mod):
    power = n
    base = 0
    curr_p = 1
    new, last = 0, 0
    n_p, l_p = 0, 0
    while power:
        if curr_p == 1:
            curr_p = 0
            new = 1
            n_p = n
        else:
            new = (last * (l_p + 1)) % mod
            n_p = (l_p * l_p) % mod
        if power & 1:
            base = (base * n_p + new) % mod
        l_p = n_p
        power >>= 1
        last = new
    return base

def ans(maxn):
    print("Getting Totient")
    tot = totient(maxn)
    print("Getting Answer")
    ans = 0
    for n in range(1, maxn + 1):
        if n % (maxn // 1000) == 0:
            print(n / maxn)
        mod = n + 1
        base = geo(n, mod)
        ans += (base * tot[n]) % mod
    return ans
print(ans(500000000))
# print(ans(100))