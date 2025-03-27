from decimal import Decimal, getcontext

# Set 50-digit precision
getcontext().prec = 50

pi = Decimal("3.14159265358979323846")

# C++ code precomputes Approx up to index 200000000.
# WARNING: 200,000,000 is extremely high for Python.
# For testing, consider using a smaller value.
MAX_INDEX = 137000000  

# Using 1-indexing (index 0 is unused)
Approx = [None] * MAX_INDEX

def approx(i: int) -> Decimal:
    return Approx[i]

def aa(n: int) -> Decimal:
    # Provided for completeness (not used in main)
    return Decimal(1) / ( (pi * Decimal(n)).sqrt() )

def shift(last: Decimal, n: int, i: int) -> Decimal:
    return last * Decimal(2) * (Decimal(n) - Decimal(i)) / (Decimal(2) * Decimal(n) - Decimal(i))

from tqdm import tqdm
def A(n: int) -> Decimal:
    # Calculate A(n) as in C++ code
    T = shift(approx(n) / Decimal(2), n, 0)
    B = approx(n - 1) / Decimal(2)
    for i in tqdm(range(n)):
        T += B
        B = shift(B, n - 1, i)
    return T

def main():
    k = 127000000
    j = 1 << 20  # This is 2^28 (the C++ comment says 2^30, but the shift is by 28)
    v = Decimal("1.9999")
    
    print("Building")
    Approx[1] = Decimal("0.5")
    # Precompute Approx values (for indices 2 to MAX_INDEX - 1)
    for i in tqdm(range(2, MAX_INDEX)):
        i_dec = Decimal(i)
        Approx[i] = Approx[i - 1] * (Decimal(2) * i_dec) * (Decimal(2) * i_dec - Decimal(1)) / (i_dec * i_dec * Decimal(4))
        if i < 127000000:
            Approx[i - 1] = None
        # Uncomment the following lines to monitor progress on smaller runs:
        # if i % 1000000 == 0:
        #     print(f"Computed Approx[{i}]")
    
    # Binary search-like loop as in C++
    while j >= 1:
        nk = k + j
        print(j, nk)
        if A(nk) * v > Decimal(1):
            k = nk
        j //= 2
    
    k += 1
    print(k, A(k) * v)

if __name__ == "__main__":
    main()
