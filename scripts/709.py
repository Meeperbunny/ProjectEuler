maxn = 8
# maxn = 24680
mod = 1020202009

fa = {}
def factorial(n):
    global fa
    if n not in fa:
        fa[n] = (factorial(n - 1) * n) % mod if n > 1 else 1
    return fa[n]

bi = {}
def binom(n, k):
    global bi
    if (n, k) not in bi:
        bi[(n, k)] = (factorial(n) * pow(factorial(k), -1, mod) * pow(factorial(n - k), -1, mod)) % mod 
    return bi[(n, k)]

dp = [[0 for _ in range(maxn + 1)] for _ in range(maxn + 1)]
dp[0][0] = 1
for n in range(1, maxn + 1):
    if n % 10 == 0:
        print(n)
    for f in range(0, n):
        dp[n][f + 1] = (dp[n][f + 1] + dp[n - 1][f]) % mod
        for k in range(2, f + 1, 2):
#             print(n, f, k)
            dp[n][f - k + 1] = (dp[n][f - k + 1] + binom(f, k) * dp[n - 1][f]) % mod
    
print(sum(dp[maxn]))