def sieve(n):
    s = [1 for _ in range(n + 1)]
    primes = []
    for q in range(2, n + 1):
        if s[q]:
            primes.append(q)
            for i in range(2 * q, n + 1, q):
                s[i] = 0
    return primes
primes = sieve(10000)
def u(n):
    for p in primes:
        if (n % p) % 7 != 0:
            return p
for i in range(1, 10 + 1):
    print(i, u(i))
def A(n):
    return sum([u(i) for i in range(1, n + 1)])

def solve(n, i, m = 1):
    T = 0
    if n == 0:
        return 0
    p = primes[i]
    cycle_len = -1
    # Find cycle len. It is at least p
    to_verify = p
    print("Finding", p)
    t = 1
    for p_c_len in range(p, n + 1, p):
        if p_c_len > t:
            print(p_c_len)
            t *= 2
        # print(i, p, p_c_len, [u((e * p_c_len) * m) for e in range(1, p_c_len + 1)])
        isg = True
        for c in range(1, p_c_len):
            if not isg:
                break
            b = u((0 * p_c_len + c) * m)
            for q in range(1, to_verify):
                if u((q * p_c_len + c) * m) != b:
                    isg = False
                    break
        if isg:
            cycle_len = p_c_len
            break    
    print("Cycle", p, "is", cycle_len)
    if cycle_len == -1:
        cycle_len = n + 1
    cnt = n // cycle_len
    R = 0
    for tp in range(1, cycle_len):
        R += u(m * tp)
    T += R * cnt
    over = n - cycle_len * cnt
    assert(over >= 0)
    print(primes[i], n, cycle_len, over, T, R)
    for tp in range(1, over + 1):
        T += u(m * tp)
    print(primes[i], n, cycle_len, over, T, R)
    T += solve(cnt, i + 1, m * cycle_len)
    return T
print(solve(10**17, 0))