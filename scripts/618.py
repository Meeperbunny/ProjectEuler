m = 24
mod = 1000000000

fib = [0, 1]
while len(fib) <= m:
    fib.append(fib[-1] + fib[-2])
fib[m]

sieve = [1 for _ in range(fib[m] + 1)]
primes = []
for i in range(2, fib[m] + 1):
    if sieve[i]:
        primes.append(i)
        for q in range(i * 2, fib[m] + 1, i):
            sieve[q] = 0

ans = [0 for _ in range(fib[m] + 1)]
ans[0] = 1
for p in primes:
    for i in range(p, fib[m] + 1):
        ans[i] = (ans[i] + ans[i - p] * p) % mod

print(sum([ans[fib[i]] for i in range(2, m + 1)]) % mod)