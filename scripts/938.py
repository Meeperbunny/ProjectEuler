from decimal import Decimal, getcontext

# Set decimal precision to 20 digits
getcontext().prec = 20

N = 24690
M = 12345
from tqdm import trange
# Create a DP table with Decimal zeros
prob = [[Decimal(0) for _ in range(M + 1)] for _ in range(N + 1)]
prob[N][M] = Decimal(1)

for n in trange(N, -1, -1):
    for m in range(M, -1, -1):
        t = n + m
        if n == 0 or m == 0:
            continue
        if t <= 1:
            continue
        # Calculate probabilities using Decimal for higher precision
        p_first_red   = Decimal(n) / Decimal(t)
        p_second_red  = Decimal(n - 1) / Decimal(t - 1)
        p_first_black = Decimal(m) / Decimal(t)
        p_second_black = Decimal(m - 1) / Decimal(t - 1)
        
        p_both_red = p_first_red * p_second_red
        p_both_black = p_first_black * p_second_black
        p_other = Decimal(1) - (p_both_red + p_both_black)
        
        # Calculate removal probabilities
        total = p_both_red + p_other  # denominator for removal probabilities
        p_remove_two_reds = p_both_red / total
        p_remove_one_black = p_other / total
        
        # Update DP table ensuring safe indices
        if n >= 2:
            prob[n - 2][m] += prob[n][m] * p_remove_two_reds
        if m >= 1:
            prob[n][m - 1] += prob[n][m] * p_remove_one_black

# Sum over the results for prob[0][i] where 1 <= i < M
T = Decimal(0)
for i in range(1, M):
    print(prob[0][i])
    T += prob[0][i]
print("T =", T)
