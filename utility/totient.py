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