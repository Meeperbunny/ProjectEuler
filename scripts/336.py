import itertools

n, m = 11, 2011

def p_to_n(p):
    return "".join([chr(ord('A') + (len(p) - e)) for e in p])

cnt = {}
def get_cnt(p):
    # print(p)
    to_f = len(p)
    if to_f == 0:
        return 0
    add = 2
    for i in range(to_f):
        # print(to_f, p[i])
        if i == to_f - 1:
            add -= 1
        if p[i] == to_f:
            # If it is at 0, then 0 + p[1:], etc...
            if i == 0:
                return 0 + get_cnt(p[1:])
            return add + get_cnt(p[i + 1:] + list(reversed(p[:i])))

def fac(n):
    return n * fac(n - 1) if n >= 1 else 1

prog = 100
max_n = fac(n)
mac = 0
cnts = []
for i, p in enumerate(itertools.permutations([i for i in range(1, n + 1)])):
    if i % (max_n // prog) == 0:
        print(i / max_n)
    cnt = get_cnt(list(p))
    if cnt > mac:
        cnts = [p]
        mac = cnt
    elif cnt == mac:
        cnts.append(p)

c_arr = [p_to_n(e) for e in cnts]
c_arr.sort()
print(mac, c_arr[m - 1])