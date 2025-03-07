inc = 10_0000
lk = [0 for _ in range(inc)]
def ttc(d):
    minc = 0
    mloss = 0
    ttc = 0
    for i in range(0, inc):
        s = str(i)
        lk[i] = sum([int(c == d) for c in s])
        ttc += lk[i]
        minc = max(minc, ttc - i)
        mloss = min(mloss, ttc - i)
        
    return ttc# , minc, mloss
from tqdm import tqdm
def solve(d):
    cnt = 0
    tot = 0
    x, y = [], []
    TC = ttc(d)
    for i in range(0, 2000_000_000_000, inc):
    # for i in tqdm(range(0, 2000_000_000_00, inc)):
        # if i % 1000 == 0:
        #     x.append(i)
        #     y.append(cnt)
        s = str(i)

        nxt_cnt = cnt + TC + inc * sum([int(c == d) for c in s])

        prev = cnt < i
        nxt = nxt_cnt < i
        if cnt == i or prev != nxt:
            # print(i, cnt, nxt_cnt)
            top_add = sum([int(c == d) for c in s])
            for q in range(0, inc):
                cnt += top_add + lk[q]
                if cnt == i + q:
                    # print(i + q)
                    tot += i + q
        cnt = nxt_cnt
    return tot
ans = 0
for d in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
    print("checking", d)
    sub_t = solve(d)
    print(f'\tgot: {sub_t}')
    ans += sub_t
print(ans)

"""
checking 1
        got: 22786974071
checking 2
        got: 73737982962
checking 3
        got: 372647999625
checking 4
        got: 741999999540
checking 5
        got: 100000000000
checking 6
        got: 2434703999430
checking 7
        got: 1876917059570
checking 8
        got: 15312327487352
checking 9
        got: 360000000000
21295121502550
"""