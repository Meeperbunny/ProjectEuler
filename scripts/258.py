m = 20092010
from tqdm import trange
def mult(A, B):
    res = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    assert len(A[0]) == len(B)
    for i in range(len(A)):
        for j in range(len(B)):
            a_ij = A[i][j]
            for q in range(len(B[0])):
                res[i][q] += a_ij * B[j][q]
                res[i][q] %= m
    return res
def gen_transition():
    transition = [[0 for _ in range(2000)] for _ in range(2000)]
    for i in range(0, 1999):
        transition[i + 1][i] = 1
    transition[0][1999] = 1
    transition[1][1999] = 1
    return transition
T = gen_transition()
base = [[1 for _ in range(2000)]]
M = mult(base, T)
def solve(k):
    B = base.copy()
    M = gen_transition()
    C = gen_transition()
    k -= 1
    while k:
        print(k)
        if k & 1:
            M = mult(C, M)
            k -= 1
        else:
            C = mult(C, C)
            k //= 2
    R = mult(B, M)[0][0]
    print(R)
    return R[0][0]
print(solve(1_000_000))