from tqdm import tqdm
def get_points(r):
    pnts = []
    for x in range(-r, r + 1):
        for y in range(-r, r + 1):
            if x**2 + y**2 < r**2:
                pnts.append((x, y))
    return pnts

K = 105
P = get_points(K)
from math import ceil, floor
eps = 0.0000000001
P.remove((0, 0))
URP = [e for e in P if e[0] > 0 and e[1] > 0]
ULP = [e for e in P if e[0] <= 0 and e[1] >= 0]
m_s = set()
cnt = 0
lk = {}
for k in range(1, K):
    lk[k] = -int((K**2 - k**2 - eps)**0.5)
for p_ur in tqdm(URP):
    for p_ul in ULP:
        for k in range(1, K):
            rb, lb = 0, -K
            if p_ul[0] == 0:
                rb = -1
            lb = max(lb, lk[k])
            t = k / p_ur[1]
            lb = max(lb, ceil(eps - (t * p_ur[0])))
            cnt += 4 * max((rb - lb + 1), 0)
print("DONE")
for p1 in tqdm(P):
    for p2 in P:
        if p1[0] > 0 and p1[1] > 0:
            if p2[0] > 0 and p2[1] > 0:
                if p1[1] * p2[0] < p2[1] * p1[0]: 
                    for k in range(1, K):
                        lb = lk[k]
                        rb = 0
                        bnds = []
                        bnds.append(k / p1[1] * (-p1[0]))
                        bnds.append(k / p2[1] * (-p2[0]))
                        # print(bnds)
                        bnds = [ceil(bnds[0] + eps), floor(bnds[1] - eps)]
                        bnds[0] = max(bnds[0], lb)
                        bnds[1] = bnds[1]
                        if bnds[1] < bnds[0]:
                            continue
                        # print(p1, p2, k, "BNDS", bnds[0], bnds[1], 4 * max(bnds[1] - bnds[0] + 1, 0))
                        cnt += 4 * max(bnds[1] - bnds[0] + 1, 0)
print(cnt)