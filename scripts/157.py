from math import gcd

def get_divs(n):
    divs = set()
    for i in range(1, int(n**0.5+1)):
        if n % i == 0:
            divs.add(n // i)
            divs.add(i)
    return sorted(list(divs))

tot = 0
s = set()
for n in range(1, 10):
    print(f"On n = {n}")
    N = 10**n
    divs = get_divs(N)
    for a in range(len(divs)):
        for b in range(a, len(divs)):
            A, B = divs[a], divs[b]
            if (gcd(A, B) == 1):
                if N * (A + B) % (A * B) == 0:
                    p = N * (A + B) // (A * B)
                    tot += len(get_divs(p))
                    # for div in get_divs(p):
                    #     s.add((A * div, B * div, p // div))
print(tot)