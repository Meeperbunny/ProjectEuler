def pfs(n):
    pfs = []
    for i in range(2, n):
        if i * i > n:
            break
        while n % i == 0:
            n //= i
            pfs.append(i)
    if n - 1:
        pfs.append(n)
    return pfs