def get_factors(n):
    facs = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            facs.add(i)
            facs.add(n // i)
    return facs

def f(n):
    n = 2**n - 1
    return get_factors(n)

N = 60
to_rm = set()
for el in get_factors(N):
    print("On", el)
    if el != N:
        to_rm = to_rm.union(f(el))

print("Getting main")
to_add = f(N)
print("Done, getting answer")

tot = 0
for el in to_add:
    if el not in to_rm:
        tot += el + 1
print("Answer:", tot)