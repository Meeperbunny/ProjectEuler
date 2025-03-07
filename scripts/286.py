from decimal import *

def points_20(q):
    dp = [[0 for _ in range(21)] for _ in range(51)]
    dp[0][0] = Decimal(1)
    for x in range(1, 50 + 1):
        p_x = Decimal(1) - Decimal(x) / Decimal(q)
#         print('\t', p_x)
        q_x = Decimal(x) / Decimal(q)
        for i in range(21):
            if i != 0:
                dp[x][i] += dp[x - 1][i - 1] * p_x
            dp[x][i] += dp[x - 1][i] * q_x
#     for row in dp:
#         print(row[0])
    return dp[50][20]

n = Decimal(1)
b = Decimal(50)
while n > 0.0000000000000001:
    while points_20(b + n) > 0.02:
        b += n
    n /= 2
b