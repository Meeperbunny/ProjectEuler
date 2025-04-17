A = [
    [1, 2, 2],
    [-2, -1, -2],
    [2, 2, 3],
]
B = [
    [1, 2, 2],
    [2, 1, 2],
    [2, 2, 3],
]
C = [
    [-1, -2, -2],
    [2, 1, 2],
    [2, 2, 3],
]

def mult(A, B):
    res = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    assert(len(A[0]) == len(B))
    for i in range(len(A)):
        for q in range(len(B[0])):
            for j in range(len(B)):
                res[i][q] += A[i][j] * B[j][q]
    return res

N = 75_000_000
tris = set()
st = [[[0, 0, 1]]]
while len(st):
    # print(st)
    c = st.pop()
    tris.add(tuple(c[0]))
    # print(c)
    c[0][0], c[0][1] = c[0][1], c[0][0]
    for el in [A, B, C]:
        t = mult(c, el)
        # print('\t', t)
        if t[0][0] > t[0][1]:
            t[0][0], t[0][1] = t[0][1], t[0][0]
        if sum(t[0]) <= N:
            if t[0][0] >= 1 and t[0][0] <= t[0][1] <= t[0][2]:
                st.append(t)
print(len(tris) - 1)