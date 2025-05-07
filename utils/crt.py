def extended_gcd(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    # Bezout
    return old_s, old_t
    # GCD
    # return old_r
    # Quotients by gcd
    # return t, s

# Arr is a list of pairs [(a_1, n_1), (a_2, n_2),...]
def chinese_remainder(arr):
    a1, n1 = 0, 1
    for a2, n2 in arr:
        p *= n2
        # Extended gcd for bezout constants
        m1, m2 = extended_gcd(n1, n2)
        a1, n1 = a1 * m2 * n2 + a2 * m1 * n1, n1 * n2
    return a1 % n2