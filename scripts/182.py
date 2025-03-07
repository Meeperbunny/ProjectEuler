from collections import Counter
from math import lcm, gcd

def getdivs(n):
    divs = []
    for i in range(1, n + 1):
        if n % i == 0:
            divs.append(i)
    return divs

def solve(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    periods = Counter()
    pdivs = getdivs(p - 1)
    qdivs = getdivs(q - 1)
    for m in range(2, n):
        # Get smallest exponent for which m^x == 1 mod p
        r_p = -1
        for p_div in pdivs:
            if pow(m, p_div, p) == 1:
                r_p = p_div
                break
        r_q = -1
        for q_div in qdivs:
            if pow(m, q_div, q) == 1:
                r_q = q_div
                break
        if r_p == -1 or r_q == -1:
            continue
        period = lcm(r_q, r_p)
        # Lcm is the period
        periods[period] += 1

    # For each i = k(period) + 1, m^i == m mod n
    evals = Counter()
    for q, period in enumerate(periods):
        inc = periods[period]
        if period <= 1:
            continue
        for i in range(period, phi, period):
            evals[i + 1] += inc

    # Get answer
    tot = 0
    min_val = min(evals.values())
    for e in range(2, phi):
        if gcd(e, phi) == 1:
            if evals[e] == min_val:
                tot += e
    return tot
                  
print(solve(1009, 3643))
# solve(19, 37)