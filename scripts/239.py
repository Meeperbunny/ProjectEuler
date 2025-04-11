from decimal import Decimal, getcontext

# Increase precision to avoid floating-point issues
getcontext().prec = 50

T = 100
PC = 25
STATE_SIZE = 1 << PC

from tqdm import trange

# Initialize 3D DP array with two layers
dp = [[[Decimal(0) for _ in range(4)] for _ in range(STATE_SIZE)] for _ in range(2)]
dp[0][0][0] = Decimal(1)

for p in range(PC):
    print(f"ON {p}")
    total_spots = T - p
    cur = p % 2
    nxt = 1 - cur

    # Clear next layer
    for s in trange(STATE_SIZE):
        for k in range(4):
            dp[nxt][s][k] = Decimal(0)

    for s in trange(STATE_SIZE):
        for k in range(3):
            if dp[cur][s][k] == 0:
                continue

            can_myself = 0
            pc = 0
            for i in range(PC):
                if (s >> i) & 1:
                    pc += 1
                elif i == p:
                    can_myself = 1

            primes_left = PC - pc
            chance_prime = Decimal(primes_left - can_myself) / total_spots
            chance_myself = Decimal(can_myself) / total_spots
            chance_normal = Decimal(1) - (chance_prime + chance_myself)

            for i in range(PC):
                if not ((s >> i) & 1):
                    new_s = s | (1 << i)
                    if i == p:
                        dp[nxt][new_s][k + 1] += dp[cur][s][k] / total_spots
                    else:
                        dp[nxt][new_s][k] += dp[cur][s][k] / total_spots

            dp[nxt][s][k] += dp[cur][s][k] * chance_normal

result = Decimal(0)
for s in range(STATE_SIZE):
    result += dp[PC % 2][s][3]

print(result)
