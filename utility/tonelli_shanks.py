def tonelli_shanks(p: int, n: int) -> int:
    """Given prime p and n such that some r exists for r^2 = n, returns such r."""
    Q = p - 1
    S = 0
    while Q % 2 == 0:
        S += 1
        Q //= 2
    z = None
    for a in range(1, p):
        if pow(a, (p - 1) // 2, p) == p - 1:
            z = a
            break
    assert(z != None)
    M = S
    c = pow(z, Q, p)
    t = pow(n, Q, p)
    R = pow(n, (Q + 1) // 2, p)

    while True:
        if t == 0:
            return 0
        elif t == 1:
            return R
        for i in range(1, M):
            if pow(t, pow(2, i, p), p) == 1:
                b = pow(c, pow(2, M - i - 1, p), p) % p
                M = i % p
                c = b * b % p
                t = t * b * b % p
                R = R * b % p
                break