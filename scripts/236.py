from fractions import Fraction
nums = [(5248, 640),
(1312, 1888),
(2624, 3776),
(5760, 3776),
(3936, 5664),
]
ASUM = sum(e[0] for e in nums)
BSUM = sum(e[1] for e in nums)
def get_incs(m, a, b):
    F = Fraction(Fraction(1, m) * Fraction(a, b))
    return F.numerator, F.denominator
def maxOrMin(a_i, b_i):
    if a_i * BSUM > b_i * ASUM:
        # If the spoilage increases with each i, then do the max, otherwise do the min
        return "MAX"
    return "MIN"

mset = set()
A, B = nums[1]

for a in range(1, A + 1):
    for b in range(a + 1, B + 1):
        a_f = Fraction(a, A)
        b_f = Fraction(b, B)
        mset.add(b_f / a_f)
        # if a_f * m == b_f:
        #     print(f"{a}/{A}, {b}/{B}")

pmset = set()
mm = Fraction(0)
for m in mset:
    isgood = True
    AT = 0
    BT = 0
    for a, b in nums:
        a_i, b_i = get_incs(m, a, b)
        # print(m, a, b)
        # If either inc is greater, then cant do
        if a_i > a or b_i > b:
            isgood = False
            break
        type = maxOrMin(a_i, b_i)
        ac, bc = a_i, b_i
        if type == "MAX":
            minc = min(a // a_i, b // b_i)
            ac = a_i * minc
            bc = b_i * minc
        # print("ACBC", ac, bc)
        AT += ac
        BT += bc
    if AT * BSUM > BT * ASUM:
        if isgood:
            # print("### M for", m)
            # print(AT, BT, ASUM, BSUM)
            # print(AT / ASUM, BT / BSUM)
            mm = max(m, mm)
            pmset.add(m)
pmlist = list(sorted(pmset))
pmlist = pmlist[pmlist.index(Fraction(1476, 1475)):]
print(len(pmlist))
from tqdm import tqdm
ic = 0
mm = Fraction(0)
for m in pmlist:
    fp = {(0, 0)}
    isg = False
    for a, b in nums[0:3]:
        is_last = (a, b) == nums[-1]
        to_add = set()
        a_i, b_i = get_incs(m, a, b)
        minc = min(b // b_i, a // a_i)
        for e in fp:
            for k in range(1, minc + 1):
                AA = e[0] + a_i * k
                BB = e[1] + b_i * k
                if AA > ASUM and BB > BSUM:
                    break
                to_add.add((AA, BB))
        fp = to_add
    sp = {(0, 0)}
    isg = False
    for a, b in nums[3:]:
        is_last = (a, b) == nums[-1]
        to_add = set()
        a_i, b_i = get_incs(m, a, b)
        minc = min(b // b_i, a // a_i)
        for e in sp:
            for k in range(1, minc + 1):
                AA = e[0] + a_i * k
                BB = e[1] + b_i * k
                if AA > ASUM and BB > BSUM:
                    break
                to_add.add((AA, BB))
        sp = to_add

    a = (m * ASUM) / BSUM * b

    bmult = Fraction(m * ASUM, BSUM)
    bd = bmult.denominator
    binc = BSUM // bd
    isg = False
    for b in range(bd, BSUM, bmult.denominator):
        if isg:
            break
        a = int(bmult * b)
        if a > ASUM:
            break
        # print(a, b)
        for e in sp:
            lk = a - e[0], b - e[1]
            if lk in fp:
                isg = True
                break
    if isg:
        mm = max(m, mm)
        ic += 1
        print(ic, end=" ")
        print(m)
        if ic == 35:
            break
print(mm)