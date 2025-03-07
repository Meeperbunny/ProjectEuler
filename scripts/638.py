m = int(1e9+7)

def ans(q, n):
    if (q == 1):
        # Handle normal case
        fac = [1 for _ in range(n * 2 + 1)]
        ifac = [1 for _ in range(n * 2 + 1)]
        
        for i in range(1, n * 2 + 1):
            fac[i] = (fac[i - 1] * i) % m
            ifac[i] = pow(fac[i], -1, m)
        # Return gaussian for normal case
        return (fac[n * 2] * ifac[n] * ifac[n]) % m
    
    qnums = [0 for _ in range(n * 2 + 1)]
    qfac = [1 for _ in range(n * 2 + 1)]
    qfacinv = [1 for _ in range(n * 2 + 1)]
    
    for i in range(n * 2 + 1):
        qnums[i] = ((1 - pow(q, i, m) + m) * pow(1 - q + m, -1, m)) % m
        if i >= 2:
            qfac[i] = (qnums[i] * qfac[i - 1]) % m
        if i >= 1:
            qfacinv[i] = pow(qfac[i], -1, m)
    
    return (qfac[n * 2] * qfacinv[n] * qfacinv[n]) % m

# ans(4, 10)

tot = 0
for k in range(1, 7 + 1):
    print(f"On k = {k}")
    tot = (tot + ans(k, 10**k + k)) % m
print(tot)