def mult(A, B, mod=None):
    res = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    assert(len(A[0]) == len(B))
    for i in range(len(A)):
        for q in range(len(B[0])):
            for j in range(len(B)):
                res[i][q] += A[i][j] * B[j][q]
                if mod:
                    res[i][q] %= mod
    return res

def matpow(m, k, mod=None):
    b = list(m)
    k -= 1
    while k:
        if k & 1:
            m = mult(b, m, mod)
            k -= 1
        else:
            b = mult(b, b, mod)
            k //= 2
    return m