mod = 1234567891
n = 10**14
# mod = 7
# n = 10**1
def frr(n, i):
    return (n + i) * (n + i - 1) // 2 - n * (n - 1) // 2
T = 0
cc = 1
while cc <= n:
    cn = n // cc
    maxnum = n // cn
    nxt = maxnum + 1
    T += frr(cc, nxt - cc) * (pow(2, n - 1, mod) - pow(2, n - (cn - 1) - 1, mod)) % mod
    cc = nxt
print(T, T % mod)