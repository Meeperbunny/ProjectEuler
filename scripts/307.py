from tqdm import tqdm
def p(k, n):
    la = [0 for _ in range(k + 3)]
    nx = [0 for _ in range(k + 3)]
    la[k] = 1
    for i in range(1, n + 1):
        p = 1 / (n - i + 1)
        ip = 1 - p
        ac = 1
        for q in range(0, k + 1):
            nx[q] = (la[q] + la[q + 1] * (q + 1) * p + la[q + 2] * (q + 2) * (q + 1) / 2 * p * p) * ac
            ac *= ip
        la, nx = nx, la
    return 1 - la[0]
# print(p(3, 7))
print(p(20_000, 1_000_000))
