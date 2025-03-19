from tqdm import tqdm
N = 10**8
mod = int(1e9+7)
fac = [1 for _ in range(2 * N + 10)]
ifac = [1 for _ in range(2 * N + 10)]
for i in tqdm(range(1, len(fac))):
    fac[i] = (fac[i - 1] * i) % mod
    ifac[i] = pow(fac[i], -1, mod)
def comb(n, k):
    return (fac[n] * ifac[n - k] * ifac[k]) % mod
def P(n, k):
    if n <= 0 or k <= 0:
        return 0
    return comb(n + k - 2, k - 1)
P(3, 3)
def C(a, b):
    if b < a:
        return 0
    return (P(a, b) - P(a - 1, b + 1) + mod) % mod
C(5, 5)
def cont(i, n):
    return C(n - i, n)
a, b = 1, 3
t = 0
la = cont(0, N)
for i in tqdm(range(1, N + 1)):
    nx = cont(i, N)
    diff = (la - nx + mod) % mod
    la = nx
    t = (t + a * diff) % mod
    a, b = b, (a + b) % mod
print(t)
