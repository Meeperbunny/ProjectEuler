
def get_divs(n):
    divs = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for q in range(i, n + 1, i):
            divs[q].append(i)
    return divs

def combine_divs(d1, d2):
    dset = set()
    for a in d1:
        for b in d2:
            dset.add(a * b)
    return list(dset)