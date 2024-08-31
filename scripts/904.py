from math import pi, atan, gcd

def ans(N, L):
    to_solve = []
    for n in range(1, N + 1):
        to_solve.append([n**(1/3), 1000, 0])
    n = 1
    sqL = L**0.5
    while n * n + 1 <= L:
        if n % 10 == 0:
            print(n / sqL)
        m = 1
        while m < n and n * n + m * m <= L:
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
            # Check if diff is lowest, if so propogate, otherwise break
            ind = 0
            j = N
            while j:
                while True:
                    if ind + j >= N:
                        break
                    if angle > to_solve[ind + j][0]:
                        ind += j
                    else:
                        break
                j >>= 1
            Q = []
            Q.insert(0, ind)
            Q.insert(0, ind + 1)
            while len(Q):
                # Check the diff
                i = Q.pop()
                if i < 0 or i >= N:
                    break
                diff = abs(to_solve[i][0] - angle)
                if diff > to_solve[i][1]:
                    continue
                elif diff < to_solve[i][1]:
                    to_solve[i][1] = diff
                    to_solve[i][2] = side_len
                elif diff == to_solve[i][1]:
                    to_solve[i][2] = max(to_solve[i][2], side_len)
                if i <= ind:
                    Q.insert(0, i - 1)
                else:
                    Q.insert(0, i + 1)
            m += 1
        n += 1
    
    print(to_solve)
    return sum([e[2] for e in to_solve])

print(ans(45000, 10**10))
# print(ans(10, 10**6))
        