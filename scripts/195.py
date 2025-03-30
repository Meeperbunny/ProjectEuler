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
def semiperimeter(a, b, c):
    return (a + b + c) / 2
def area(a, b, c):
    s = semiperimeter(a, b, c)
    return (s * (s - a) * (s - b) * (s - c))**0.5
def incircle_radius(a, b, c):
    return area(a, b, c) / semiperimeter(a, b, c)
from tqdm import tqdm
N = 1053779
cnt = 0
M = 4
D = get_divs(M * N)
for j in tqdm(range(1, M * N + 1)):
    divs = D[j]
    jsq = j * j
    divs_jsq = combine_divs(divs, divs)
    for D1 in divs_jsq:
        D2 = jsq // D1
        A = (D1 + 2 * j)
        B = (D2 + 2 * j)
        if A % 3 != 0 or B % 3 != 0:
            continue
        A //= 3
        B //= 3
        a, b, c = A, B, (A + B - j)
        r = incircle_radius(a, b, c)
        if r <= N and A != B:
            cnt += 1
print(cnt // 2)