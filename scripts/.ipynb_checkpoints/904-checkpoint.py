from math import pi, atan, gcd

def ans(N, L):
    to_solve = []
    for n in range(1, N + 1):
        to_solve.append([n**(1/3), 1000, 0])

    thetas = []
    n = 1
    sqL = L**0.5
    while n * n + 1 <= L:
        if n % 10 == 0:
            print(n / sqL)
        m = 1
        while m < n and n * n + m * m <= L:
            if (m + n) & 1 and gcd(m, n) == 1:
                a = n * n - m * m
                b = 2 * m * n
                c = n * n + m * m
                # print(a, b, (n * n + m * m))
                # Find the max triple you can get given this primative
                # Add the angle theta and the side lengths
                mult = L // c
                max_a = a * mult
                max_b = b * mult
                max_c = c * mult
                # Calc everything
                theta_p = 2 * pi - (pi / 2 + atan(2 * max_b / max_a) + atan(2 * max_a / max_b))
                theta = pi - theta_p
                
                angle = theta / pi * 180
                side_len = max_a + max_b + max_c

                # Binary search
                for i in range(to_solve + 1):
                    lower, upper = -1000000000, 1000000000
                    if 0 < i:
                        lower = to_solve[i - 1][0]
                    if i < len(to_solve):
                        upper = to_solve[i][0]
                        
                
            m += 1
        n += 1
    return thetas

# print(ans(45000, 10**10))
print(ans(100, 10**6))
        