maxn = 1000_000_000

def comp(n, k):
    return n // k - 1

print("Creating Totient Array")
totient = [1 for _ in range(maxn + 1)]
print("Generating Totient")
for p in range(2, maxn + 1):
    if totient[p] == 1:
        # Is prime
        k = 1
        while p**k < maxn:
            inc = p**k
            change = p
            if k == 1:
                change = p - 1
                
            for q in range(inc, maxn + 1, inc):
                totient[q] *= change
            k += 1
print("Done Generating Totient")

print("Computing Hidden")
hidden = 0
for i in range(1, maxn + 1):
    hidden += 6 * (totient[i] * comp(maxn, i))
print("Answer:", hidden)