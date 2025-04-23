
def get_divs(n):
    divs = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for q in range(i, n + 1, i):
            divs[q].append(i)
    return divs