def solve(maxn):
    print("Initalizing Divs")
    divs = [[] for i in range(maxn + 1)]

    print("Getting Divs")
    for i in range(1, int(maxn**0.5+1)):
        for q in range(i, maxn + 1, i):
            divs[q].append(i)
            divs[q].append(q // i)
        divs[i] = sorted(list(set(divs[i])))
    print("Done Getting Divs")
    # divs
    M = [1 for _ in range(maxn + 1)]
    M[0] = 0
    M[1] = 0
    for i in range(2, maxn + 1):
        if i % 100_000 == 0:
            print(i)
        f = i
        s = i - 1
        tdivs = set()
        for d1 in divs[f]:
            for d2 in divs[s]:
                m = d1 * d2
                if m > i and m <= maxn:
                    M[m] = i
    return sum(M)
# print(solve(10_000_000))
print(solve(10_000_000))
