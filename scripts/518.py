def ans(n):
    print("Constructing")
    sieve = [1 for _ in range(n + 1)]
    primes = []
    print("Sieve")
    for i in range(2, n + 1):
        if sieve[i]:
            primes.append(i)
            for q in range(i * 2, n + 1, i):
                sieve[q] = 0
    pset = set(primes)

    divs = [[] for _ in range(n + 1)]
    print("Getting Divs")
    for i in range(1, n + 1):
        if i < 100:
            print(i)
        for q in range(i, n + 1, i):
            if q - 1 in pset:
                divs[q].append(i)

    print("Comuting Square Divs")
    tot = 0
    addset = set()
    for p in primes:
        Q = p + 1
        # Computer square divs for P
        sqdivs = []
        for i, a in enumerate(divs[Q]):
            for b in divs[Q][i + 1:]:
                S = a * b
                if S >= Q:
                    break
                # sqdivs.append(s)
                # If a * b - 1 is a prime,
                if S - 1 in pset:
                    R = Q * Q // S
                    if R - 1 in pset:
                        addset.add((S - 1, Q - 1, R - 1))
    print("Getting Answer")
    return sum([sum(e) for e in addset])
print(ans(100000000))