def get_tables(a, b, n):
    # Given a tuple t, give its "lasts"
    lasts = {}
    sizes = {}
    sums = {}
    # a = 2
    # b = 3
    def swap(k):
        return b if k == a else a
    def swap_all_but_last(t):
        rt = []
        for i in range(len(t)):
            if i == len(t) - 1:
                rt.append(t[i])
            else:
                rt.append(swap(t[i]))
        return rt
    def swap_last(t):
        rt = []
        for i in range(len(t)):
            if i != len(t) - 1:
                rt.append(t[i])
            else:
                rt.append(swap(t[i]))
        return rt
    bt = []
    sz = 0
    def solve_for(seq):
        pre = seq[:-1]
        cnt = 0
        ss = 0
        if len(pre):
            for i in range(seq[-1]):
                cnt += get_sizes(tuple(pre))
                ss += get_sums(tuple(pre))
                pre = get_lasts(tuple(pre)) + (seq[-2],)
                pre = swap_all_but_last(pre)
        else:
            cnt = 1
            ss = seq[0]
        pre = swap_all_but_last(pre)
        pre = tuple(pre)
        lasts[seq] = pre
        sizes[seq] = cnt
        sums[seq] = ss
    def get_lasts(t):
        if t not in lasts:
            solve_for(t)
        return lasts[t]
    def get_sizes(t):
        if t not in sizes:
            solve_for(t)
        return sizes[t]
    def get_sums(t):
        if t not in sums:
            solve_for(t)
        return sums[t]
    return get_lasts, get_sizes, get_sums
def answer(a, b, n):
    def swap(k):
        return b if k == a else a
    def swap_all(t):
        rt = []
        for i in range(len(t)):
            rt.append(swap(t[i]))
        return rt
    def swap_all_but_last(t):
        rt = []
        for i in range(len(t)):
            if i == len(t) - 1:
                rt.append(t[i])
            else:
                rt.append(swap(t[i]))
        return rt
    get_lasts, get_sizes, get_sums = get_tables(a, b, n)
    # If it is greater than our current, just use current and go to next.
    csum = 0
    ct = []
    while True:
        ct += [a]
        if n < get_sizes(tuple(ct)):
            break
        # print(a, b, get_sizes(tuple(ct)) / n)
    while n:
        # print(ct, n, sizes[tuple(ct)])
        if n >= get_sizes(tuple(ct)):
            # Use all of ct. Go to next of ct.
            # print("Adding", ct, sums[tuple(ct)])
            n -= get_sizes(tuple(ct))
            csum += get_sums(tuple(ct))
            nt = get_lasts(tuple(ct))
            nt = tuple(swap_all(nt) + [ct[-1]])
            ct = list(nt)
        else:
            # Break current down by 1?
            ct = ct[0:-1]
    return csum
from tqdm import trange
T = 0
n = 22332223332233

assert(answer(5, 8, 10**6) == 6499871)
assert(answer(4, 2, 10**4) == 30004)
assert(answer(2, 3, 10) == 25)

for a in range(2, 223 + 1):
    for b in range(2, 223 + 1):
        print("Solving a = {} b = {}".format(a, b))
        if a != b:
            T += answer(a, b, n)
print(T, T % 2233222333)