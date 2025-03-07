from collections import Counter

def prime_count(n):
    s = [1 for _ in range(n + 1)]
    pi = [0 for _ in range(n + 1)]
    s[0], s[1] = 0, 0
    primes = set()
    for q in range(2, n + 1):
        if s[q]:
            primes.add(q)
            for i in range(2 * q, n + 1, q):
                s[i] = 0
    
    for i in range(1, n + 1):
        pi[i] = pi[i - 1] + s[i]
    return pi, primes

n = 100000000
m = int(1e9 + 7)

print("Starting Sieve and pi")
pi, pset = prime_count(n)
print("Done Sieve and pi")


print("Doing other shit")

maxpi = pi[-1]
maxc = 16

tot_cnts = [0 for _ in range(maxc)]
cnts = [None for _ in range(maxpi + 1)]
cnts[0] = [0 for _ in range(maxc)]
for i in range(1, n + 1):
    if i % (n // 1000) == 0:
        print(i / n)

    prev = pi[i]
    arr = [0 for _ in range(maxc)]
    if i in pset:
        # Do not add one to previous values
        for q in range(maxc):
            arr[q] += cnts[prev][q]
        arr[0] += 1
        # pset.remove(i)
    else:
        # Add 1 to previous values
        for q in range(maxc - 1):
            arr[q + 1] += cnts[prev][q]
        arr[1] += 1
    
    
    for q in range(maxc):
        tot_cnts[q] = (tot_cnts[q] + arr[q]) % m
    if i in pset:
        tot_cnts[0] -= 1
    else:
        tot_cnts[1] -= 1

    if i <= maxpi:
        cnts[i] = arr.copy()

print(tot_cnts)

b = 1
for q in range(maxc):
    if tot_cnts[q]:
        b = (b * tot_cnts[q]) % m
print(b)