def sieve(n):
    s = [1 for _ in range(n + 1)]
    primes = []
    for q in range(2, n + 1):
        if s[q]:
            primes.append(q)
            for i in range(2 * q, n + 1, q):
                s[i] = 0
    return primes
def get_divs(n):
    divs = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for q in range(i, n + 1, i):
            divs[q].append(i)
    return divs
###    2  3  4  5  6  7  8
#  2   5  9 15 21 27 33 39
#  3   9 13 17 23 29 35  
#  4  15 17 21 25 31 37   
#  5  21 23 25 29 33 39
#  6  27 29 31 33 37 43
#  7  
#  8               
# Add 2 for lower. 
primes = sieve(10**6)
cnts = [0 for _ in range(8)]
cnt = 5
def inc(c):
    if c == 5:
        return 9
    else:
        return c + 6
T = 0
from tqdm import tqdm
for p in tqdm(primes):
    togo = p * p - cnt
    skip = togo // 24
    cnt += skip * 6 * 4
    cnts[0] += skip
    cnts[1] += skip
    cnts[2] += skip
    cnts[3] += skip
    while cnt < p * p:
        cnt = inc(cnt)
        cnts[cnt % 8] += 1
    T += cnts[(p * p) % 8]
print(2 * T)