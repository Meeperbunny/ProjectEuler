s_i = 14025256
def S():
    global s_i
    ts = s_i
    s_i = s_i**2 % 20300713
    return ts
ss = []
def num(n):
    global ss
    while len(ss) <= n:
        ss += [ord(c) - ord('0') for c in str(S())]
    return ss[n]

from tqdm import trange
# Get the cyclicalities for starting positions 1 to 80

N = 5 * 10**8
K = 100
lks = [2000 for _ in range(428072426 * 5 + 200_000)]
nums = [0 for _ in range(K + 1)]
seens = [[] for _ in range(K + 1)]
for i in trange(0, N + 1):
    n = num(i)
    for k in range(0, min(i + 1, K + 1)):
        nums[k] += n
        # if nums[k] not in lks:
        #     lks[nums[k]] = k + 1
        lks[nums[k]] = min(lks[nums[k]], k + 1)
inds = [[] for _ in range(K + 1)]
for i in trange(1, N + 1):
    if lks[i] != 2000:
        inds[lks[i]].append(i)
    else:
        print("DOESNT WORK", i)
def diff(a):
    return [a[i + 1] - a[i] for i in range(len(a) - 1)]
cc = {}
for i in range(1, K + 1):
    d = diff(inds[i])
    v = min(len(d) // 2, 100)
    if len(d) == 1:
        cc[i] = 1
        continue
    for k in range(1, len(d) - v):
        if d[:v] == d[k:k+v]:
            cc[i] = k
            break

TAR = 2 * 10**15
T = 0
for e in cc:
    d = diff(inds[e])
    start = inds[e][0]
    length = sum(d[:cc[e]])

    times = max((TAR - start) // length, 0)
    T += times * cc[e] * e

    print("CYC", e)
    print(d[0:10])
    print(start, length, cc[e])
    print(times)

    curr = start + length * times
    for i in range(0, cc[e]):
        if curr > TAR:
            break
        T += e
        curr += d[i]
    # print("CYC START", inds[e][0], cc[e])
    # print(d[0:10])
print("LOWER", T)
