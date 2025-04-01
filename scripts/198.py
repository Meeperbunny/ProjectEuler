import sys
from fractions import Fraction

RRR = 3000
# Global set to hold fractions (each fraction is stored as a Fraction object)
S = set()
B = Fraction(1, 100)

def pseudo_mean(a: Fraction, b: Fraction) -> Fraction:
    """Computes the pseudo-mean: (a.num + b.num) / (a.den + b.den), simplified."""
    return Fraction(a.numerator + b.numerator, a.denominator + b.denominator)

def mean(a: Fraction, b: Fraction) -> Fraction:
    """Computes the arithmetic mean: (a + b) / 2."""
    return (a + b) / 2

C = 0
def traverse_iter(D: int, L: Fraction, M: Fraction, R: Fraction, last_moves) -> None:
    global C, RR
    """
    Iteratively computes new fractions and stores them in S,
    emulating the recursive traverse function using a stack.
    """
    # Each element on the stack is a tuple: (L, M, R, last_moves)
    stack = [(L, M, R, last_moves, 0)]
    
    while stack:
        L, M, R, last_moves, dep = stack.pop()
        
        if dep > 500:
            continue
        if M.denominator**2 > D * 5000:
            continue

        m = mean(L, R)
        if m.denominator <= D:
            S.add(m)
                
        # Compute the pseudo-means.
        lm = pseudo_mean(L, M)
        rm = pseudo_mean(M, R)
        
        # Push the two new states onto the stack.
        stack.append((L, lm, M, (M, last_moves[1]), dep + 1))
        stack.append((M, rm, R, (last_moves[0], M), dep + 1))

# 250 ->  52034410
# 600 ->  52213617
# 1000 -> 52296515
# 2000 -> 52368612
# 5000 -> 52374425

def main():
    global S
    D = 1_00_000_000
    L = Fraction(0, 1)
    M = Fraction(1, 100)
    R = Fraction(1, 99)

    from tqdm import trange
    for i in range(2, D + 1, 2):
        S.add(Fraction(1, i))
    print("T")
    
    traverse_iter(D, L, M, R, (R, L))

    C = 0
    lower_f = Fraction(1, 100)
    for e in S:
        if e.denominator <= D and e < lower_f:
            C += 1
    print(C)

if __name__ == '__main__':
    RRR = 5000
    main()