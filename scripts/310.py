from math import log2

def ans(n):
    grundy = [0 for _ in range(n + 1)]
    max_nimber = int(pow(2, int(1+log2(int(n**0.5+1)))))
    # print(max_nimber)
    for i in range(1, n + 1):
        q = 1
        c_nims = [0] * max_nimber
        while i - q * q >= 0:
            c_nims[grundy[i - q * q]] = 1
            q += 1
        for q in range(max_nimber):
            if not c_nims[q]:
                grundy[i] = q
                break
    # Collect grundys
    pre_nim = [[0 for _ in range(max_nimber)] for _ in range(n + 1)]
    nxt_nim = [[0 for _ in range(max_nimber)] for _ in range(n + 1)]
    last_nim = [[0 for _ in range(max_nimber)] for _ in range(n + 1)]

    # Construct Prefix for first
    for i, e in enumerate(grundy):
        if i:
            pre_nim[i] = pre_nim[i - 1].copy()
        pre_nim[i][e] += 1

        for q in range(max_nimber):
            # print(e ^ q, nxt_nim[i])
            nxt_nim[i][e ^ q] += 1 * pre_nim[i][q]

    # Construct last
    for i, e in enumerate(grundy):
        if i:
            for q in range(max_nimber):
                nxt_nim[i][q] += nxt_nim[i - 1][q]

        for q in range(max_nimber):
            last_nim[i][e ^ q] += 1 * nxt_nim[i][q]

    tot = 0
    for e in last_nim:
        tot += e[0]
    return tot
print(ans(100000))