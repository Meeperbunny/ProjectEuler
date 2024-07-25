m_dc = 59049  # 3^10
dp = [[[0 for _ in range(m_dc)] for _ in range(11)] for _ in range(21)]

dp[0][0][0] = 1

for d in range(20):
    for carry in range(11):
        for dused in range(m_dc):
            if d == 1 and dp[d][carry][dused]:
                print(d, carry, dused, dp[d][carry][dused])
            # At current, add a new digit. Use the carry and update dused accordingly.
            c_dc_m = 1
            for d_a in range(10):
                c_dc = (dused // c_dc_m) % 3
                if c_dc < 2:
                    # Can add
                    n_c = (carry + 11 * d_a) // 10
                    new_dused = dused + c_dc_m
                    dp[d + 1][n_c][new_dused] += dp[d][carry][dused]
                c_dc_m *= 3

print(dp[20][0][m_dc - 1])
