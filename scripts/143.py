import numpy as np

def get_last(a, b):
    x = a + np.cos(np.pi / 3) * b
    y = np.sin(np.pi / 3) * b
    return (x**2 + y**2)**0.5

def get_p(a, q):
    A = 2 * np.pi / 3
    Q = np.arcsin((q * np.sin(A)) / (a))
    return q * np.sin(np.pi / 3 - Q) / np.sin(Q)

maxn = 120_000
# maxn = 300
left = set([i for i in range(1, maxn + 1)])
left = set([784, 836])
ans = set()
for a in range(399, maxn):
    if a % (maxn // 100) == 0:
        pr = (a // (maxn // 100))
        print(pr * "#" + '.' * (100 - pr))
    for q in range(1, a):
        r = get_p(a, q)
        if np.isclose(r, round(r), rtol=1e-014):
            r = round(r)
            to_rm = []
            for t in left:
                tot = t
                p = tot - q - r
                if p <= 0:
                    continue
                if t < a:
                    to_rm.append(t)
                    continue
                tot = p + q + r
                b = get_last(q, p)
                c = get_last(r, p)
                if np.isclose(b, round(b), rtol=1e-014) and np.isclose(c, round(c), rtol=1e-014):
                    print(a, b, c, p, q, r)
                    print("Triangle with", tot, "is good")
                    ans.add(tot)
                    to_rm.append(t)
            for el in to_rm:
                left.remove(el)
print(sum(ans))  