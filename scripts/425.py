maxn = 10000000

primes = set()
sieve = [1 for _ in range(maxn + 1)]
for i in range(2, maxn + 1):
    if sieve[i]:
        primes.add(i)
        for q in range(i * 2, maxn + 1, i):
            sieve[q] = 0

def getCon(p):
    con = set()
    s = str(p)
    for i in range(len(s)):
        for q in range(10):
            t = s
            t = t[:i] + str(q) + t[i + 1:]
            sl = len(t)
            t = int(t)
            if len(s) == len(str(t)) and t in primes and t != p:
                con.add(t)
    for q in range(10):
        t = s
        tf = str(q) + t
        # tl = t + str(q)
        tf = int(tf)
        # tl = int(tl)
        if tf in primes and tf != p:
            con.add(tf)
        # if tl in primes and tl != p:
        #     con.add(tl)
    return con

adj = {}

print("Connecting Primes")
for i, p in enumerate(primes):
    # Check primes and connect
    if i % (len(primes) // 100) == 0:
        print(i / len(primes))
    for e in getCon(p):
        if p not in adj:
            adj[p] = set()
        if e not in adj:
            adj[e] = set()
        adj[e].add(p)
        adj[p].add(e)

print("Assignging Maxes")
mael = {}
for p in primes:
    mael[p] = maxn + 1
mael[2] = 2

print("QUeueing")
Q = []
Q.insert(0, (2, 2))
while len(Q):
    c, mav = Q.pop()
    for e in adj[c]:
        n_mav = max(mav, e)

        if n_mav < mael[e]:
            mael[e] = n_mav
            Q.insert(0, (e, n_mav))
    # Pass along the max element in the chain

print("SUMMING")
tot = sum(primes)
for e in mael:
    if e == mael[e]:
        tot -= e
    # else:
    #     print("P", e)

print("Answer:", tot)