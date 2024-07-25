maxn = 10_000
m = int(1e9+7)

fibs = [1, 1]
while fibs[-1] < maxn * 2:
    fibs.append(fibs[-1] + fibs[-2])
fibs

fibsSq = set([e * e for e in fibs])

paths = []

for i in range(0, maxn + 1):
    if i % (maxn // 100) == 0:
        print(i / maxn)
    for q in range(0, maxn + 1):
        if i * i + q * q in fibsSq:
            paths.append((i, q))

paths

len(paths)

cnts = [[0 for _ in range(maxn + 1)] for _ in range(maxn + 1)]
cnts[0][0] = 1
for i in range(0, maxn + 1):
    if i % (maxn // 100) == 0:
        print(i / maxn)
    for q in range(0, maxn + 1):
        for p in paths:
            if i + p[0] <= maxn and q + p[1] <= maxn:
                cnts[i + p[0]][q + p[1]] = (cnts[i + p[0]][q + p[1]] + cnts[i][q]) % m
print(cnts[maxn][maxn])