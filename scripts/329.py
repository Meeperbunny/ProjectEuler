N = 500
seq = "".join(list(reversed("PPPPNNPPPNPPNPN")))

from math import gcd

is_prime = [True for _ in range(N + 1)]
is_prime[0], is_prime[1] = False, False
for i in range(2, N + 1):
    if is_prime[i]:
        for q in range(2 * i, N + 1, i):
            is_prime[q] = False
            
def add(f1, f2):
    n, d = f1[0] * f2[1] + f2[0] * f1[1], f1[1] * f2[1]
    g = gcd(n, d)
    return n // g, d // g

def mult(f1, f2):
    n, d = f1[0] * f2[0], f1[1] * f2[1]
    g = gcd(n, d)
    return n // g, d // g

dp = [[[0, 1] for _ in range(N + 1)] for _ in range(len(seq))]

for seq_c in range(len(seq)):
    for i in range(1, N + 1):
        # If is one correct tile, then have higher chance to be right.
        is_corr = (seq[seq_c] == 'N') ^ (is_prime[i])
        p_corr = (2, 3) if is_corr else (1, 3)
        # Given chance that current is right, consider chance for (i - 1, k - 1) and (i + 1, k - 1)
        # dp[i][k] represents landing at i with k jumps left you are right.
        # Drawing from downards represents a "jump".
        # If at seq_c = 0, then can't go down. Mult stays 1.
        m = (1, 1)
        if seq_c != 0:
            if i == 1:
                m = dp[seq_c - 1][i + 1]
            elif i == N:
                m = dp[seq_c - 1][i - 1]
            else:
                m = add(mult((1, 2), dp[seq_c - 1][i - 1]), mult((1, 2), dp[seq_c - 1][i + 1]))
#         print(m, p_corr)
        dp[seq_c][i] = mult(m, p_corr)
    
tot = (0, 1)
for i in range(1, N + 1):
    tot = add(tot, mult(dp[len(seq) - 1][i], (1, N)))
print(f"Answer: {tot[0]}/{tot[1]}")