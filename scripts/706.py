from collections import Counter
mod = int(10**9+7)
from tqdm import *
# (a, b, c, a', b', c') abc is fcnts, a'b'c' is bcnts

cnts = Counter({
    (0, 0, 0, 0, 0, 0): 1,
})
D = 10**5
t = 0
cucnts = 0
for dpos in range(D):
    cc = 0
    # Add each digit here
    new_cnts = Counter()
    for d in range(0 if dpos != D - 1 else 1, 10):
        # print(dpos, d)
        for e, cnt in cnts.items():
            # Add cnts to bcnts
            new_bcnts = ((e[i] + e[i + 3]) % 3 for i in range(3))
            # Add digits to fcnts
            new_fcnts = ((e[(i + 3 - d) % 3] + int(d % 3 == i)) % 3 for i in range(3))
            # Add to cnts
            new_t = (*new_fcnts, *new_bcnts)
            new_cnts[new_t] += cnt
            new_cnts[new_t] %= mod
    # For each el in cnts, add it
    for e, cnt in new_cnts.items():
        if (e[0] + e[3]) % 3 == 0:
            cc += cnt
            cc %= mod
    if dpos + 1 == D:
        print(dpos + 1, cc)
    t += cc
    cnts = new_cnts.copy()
    # for e in cnts:
    #     print(dpos, e, cnts[e], "DOING" if (e[0] + e[3]) % 3 == 0 else "N")
# print(t)