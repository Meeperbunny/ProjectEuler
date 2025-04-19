def gci(s: str):
    return s.index('P')
def itoc(i: int) -> tuple:
    return (i // 4), i % 4
def ttoi(t: tuple) -> int:
    return t[0] * 4 + t[1]
def displayState(s):
    for i in range(4):
        for q in range(4):
            print(s[i * 4 + q] if s[i * 4 + q] != 'P' else ' ', end="")
        print()
trs = [
    (-1, 0, 68),
    (1, 0, 85),
    (0, 1, 76),
    (0, -1, 82),
]
md = {}
Q = []

Q.insert(0, (tuple((c for c in "PRBBRRBBRRBBRRBB")), 0))
md[tuple(c for c in "PRBBRRBBRRBBRRBB")] = [0, [0]]
ta = 1
i = 1
lc = 0

target = "PBRBBRBRRBRBBRBR"
t_t = tuple(c for c in target)
while len(Q):
    # if i % 10 == 0:
    #     print(len(Q), len(Q) - lc)
    #     lc = len(Q)
    i += 1
    state, d = Q.pop()
    if len(md[state][1]) == 0:
        continue
    if "".join(state) == target:
        print(sum(md[t_t][1]))
        break
    # Bfs here?
    gi = gci(state)
    cp = itoc(gi)
    stl = list(state)
    mod = int(1e8+7)
    for t in trs:
        ccp = cp[0] + t[0], cp[1] + t[1]
        if ccp[0] < 0 or ccp[0] >= 4 or ccp[1] < 0 or ccp[1] >= 4:
            continue
        # Swap the pos
        ind = ttoi(ccp)
        stl[gi], stl[ind] = stl[ind], stl[gi]

        stt = tuple(stl)

        if stt not in md:
            md[stt] = [d + 1, []]
        if d + 1 == md[stt][0]:
            md[stt][1] += [(e * 243 + t[2]) % mod for e in md[state][1]]
            Q.insert(0, (stt, d + 1))

        stl[gi], stl[ind] = stl[ind], stl[gi]
    md[state][1] = []
    