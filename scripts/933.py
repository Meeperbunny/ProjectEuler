N = 123
M = 1234567
def mex(s):
    for i in range(0, len(s) + 1):
        if i not in s:
            return i
grundy = {}
winning_moves = {}
def ways(W, H):
    global winning_moves, grundy
    if (W, H) not in winning_moves:
        for i in range(1, W + 1):
            for q in range(1, H + 1):
                if (i, q) in winning_moves:
                    continue
                C = 0
                if i == 1 or q == 1:
                    grundy[(i, q)] = 0
                s = set()
                for a in range(1, i // 2 + 1):
                    for b in range(1, q // 2 + 1):
                        nimber =    grundy[(a, b)] ^ grundy[(i - a, b)] ^ \
                                    grundy[(a, q - b)] ^ grundy[(i - a, q - b)]
                        if nimber == 0:
                            # print(i, q, a, b)
                            TA = 4
                            if a * 2 == i:
                                TA //= 2
                            if b * 2 == q:
                                TA //= 2
                            C += TA
                        s.add(nimber)
                grundy[(i, q)] = mex(s)
                winning_moves[(i, q)] = C
                grundy[(q, i)] = mex(s)
                winning_moves[(q, i)] = C
    return winning_moves[((W, H))]
def tri(n):
    return n * (n + 1) // 2
T = 0
for q in range(1, N + 1):
    z = []
    i = 0
    k = 10
    while True:
        i += 1
        z.append(ways(q, i))
        R = None
        if i > k:
            isg = True
            for j in range(i - k, i - 1):
                if z[j+1] != q - 1 + z[j]:
                    isg = False
                    break
            if isg:
                R = i - k + 1
                break
    CR = 0
    for i in range(1, R):
        CR += ways(q, i)
    L = M - R + 1
    print("R", q, R, CR)
    CR += ways(q, R) * L + tri(L - 1) * (q - 1)
    print(q, CR)
    T += CR
print(T)