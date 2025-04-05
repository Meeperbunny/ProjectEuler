from tqdm import trange
from math import ceil
def solve(n):
    B = 1 + 2 * n * (n + 1) - 2 * n - 1 - n**2 // 2
    epsilon = 0.000000001
    R = (2**0.5)*(n/4)/2
    for c in trange(1, n // 2):
        # print(c, R**2 - (R - 1/(2**0.5)*c)**2)
        y = (R**2 - (R - 1/(2**0.5)*c)**2)**0.5
        if c & 1:
            y += 1/2**0.5
        B += int(2 * ((y - epsilon) // (2**0.5)))
        # print(c, (y - epsilon) // (2**0.5))
    return B

print(solve(10**9))