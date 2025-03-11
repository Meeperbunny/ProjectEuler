from tqdm import tqdm

def sieve(n):
    s = [1 for _ in range(n + 1)]
    primes = []
    for q in range(2, n + 1):
        if s[q]:
            primes.append(q)
            for i in range(2 * q, n + 1, q):
                s[i] = 0
    return primes

def concat(n):
    primes = sieve(n)
    s = "".join([str(p).replace('0', '') for p in primes])
    # print(s)
    return s

def get_divs(n):
    divs = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for q in range(i, n + 1, i):
            divs[q].append(i)
    return divs

def solve(n):
    s = concat(n)
    divs = get_divs(10)
    d = {}
    for i in range(1, 10):
        d[chr(i + ord('0'))] = divs[i]
    mod = int(1e9+7)
    cnts = [0 for _ in range(10)]
    seq_cnt = 1
    ans = 0
    for i in tqdm(range(len(s))):
        c = s[i]
        t_divs = d[c]
        # Multiplies each by # of divs
        div_cnt = len(t_divs)
        next_cnts = [cnts[i] * div_cnt for i in range(10)]
        ans *= div_cnt
        for div in t_divs:
            # Adds itself by seq cnt
            next_cnts[div] += seq_cnt
            # Adds num of inversions of all greater than it
            ans += sum(cnts[div+1:10])
        # Mults seq cnt by # of divs
        ans = ans % mod
        # print(next_cnts, ans)
        seq_cnt *= div_cnt
        seq_cnt %= mod
        for i in range(len(next_cnts)):
            next_cnts[i] = next_cnts[i] % mod
        cnts = next_cnts.copy()
    return ans

print(solve(10**8))