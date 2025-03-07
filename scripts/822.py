# For each index, try to get it such that it is the smallest. There will be some equal to it, and make sure that all are either equal or above,
# given that the current one has undergone X operations. Once you do this, wiggle room is (# Equal - 1), and range of acceptable is: [K, K + WR].
# If 1e16 is in this range, then is good.

# n, t = 5, 7
# n, t = 10, 100
n, t = 10**4, 10**16
m = 1234567891

def c_ops(b, pa):
    a, ops = pa
    t = 0
    while a < b:
        t -= 1
        a = a * a
    while b < a:
        t += 1
        b = b * b
    return max(0, t + ops)

def tryIndex(i, l, t):
    # Binary search for Just below or equal to
    # If not in range, then is bad, otherwise return sum
    b_ops = -1
    toadd = 10**16
    opcnt = [0 for _ in l]
    goc = []
    while toadd >= 1:
        while True:
            m_ops = b_ops + toadd
            t_ops = 0
            val = (l[i], m_ops)
            for ind, e in enumerate(l):
                # print(i, e, c_ops(e, val), val, m_ops)
                opcnt[ind] = c_ops(e, val)
                t_ops += opcnt[ind]
            # print(i, m_ops, t_ops, opcnt)
            if t_ops <= t:
                b_ops += toadd
                goc = opcnt.copy()
            else:
                break
        toadd //= 2
    # TODO, get number that are the same
    m_v = (l[i], b_ops)
    s_cnt = 0
    # print(i, b_ops, goc)
    for ind, el in enumerate(goc):
        bv = [l[i], b_ops]
        nv = [l[ind], goc[ind]]
        while nv[0] < bv[0]:
            nv[0] = nv[0] * nv[0]
            nv[1] -= 1
        while bv[0] < nv[0]:
            bv[0] = bv[0] * bv[0]
            bv[1] -= 1
        s_cnt += bv[0] == nv[0] and bv[1] == nv[1]
    lower = sum(goc)
    upper = lower + s_cnt - 1
    # print(i, b_ops, goc, lower, upper)
    if lower <= t and t <= upper:
        # Get sum
        total = 0
        for ind, el in enumerate(goc):
            total += pow(l[ind], pow(2, el, m - 1), m)
        total += (t - lower) * (pow(l[i], pow(2, b_ops + 1, m - 1), m) - pow(l[i], pow(2, b_ops, m - 1), m))
        return total % m
    else:
        return False

l = list(range(2, n + 1))
toc = [True] * len(l)
for i in range(len(l)):
    print(i)
    if not toc[i]:
        continue
    s = tryIndex(i, l, t)
    if s:
        print(s)
        break
    else:
        q = i + 2
        while q - 2 < len(toc):
            toc[q - 2] = False
            q = q * q