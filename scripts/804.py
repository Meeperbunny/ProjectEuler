

from tqdm import *
from collections import Counter
from decimal import Decimal, getcontext, ROUND_CEILING
getcontext().prec = 50

k = 16

lower = -int(0.16*10**(k//2))
upper = int(0.16*10**(k//2)) + 1
bound = Decimal(10)**k
tot = 0
C = Counter()
min_y = 10000000000000
max_y = -1000000000000
for y in tqdm(range(lower, upper)):
    b = Decimal(y)
    c = Decimal(41)*Decimal(y)**2 - Decimal(1)
    # Check the number of intercepts
    lower_intercepts = None
    if b * b < Decimal(4)*c:
        # No intercepts, get the range
        lower_intercepts = None
    elif b * b == Decimal(4)*c:
        # One intercept
        lower_intercepts = None
    else:
        # Two intercepts
        sq = (b * b - Decimal(4)*c).sqrt()
        right = ((-b + sq)/Decimal(2)).to_integral_value(rounding=ROUND_CEILING)
        left = int(( -b - sq )/Decimal(2))
        lower_intercepts = [left, int(right)]
    
    # Now check against upper   
    b = Decimal(y)
    c = Decimal(41)*Decimal(y)**2 - bound
    upper_intercepts = None
    
    # Check the number of intercepts
    upper_intercepts = None
    to_add = 0
    if b * b < Decimal(4)*c:
        # No intercepts, doesn't contribute
        upper_intercepts = None
    elif b * b == Decimal(4)*c:
        # One intercept, check that b is even, otherwise is non-integer
        if y % 2 == 0:
            tot += 1
        # upper_intercepts = None
    else:
        # Two intercepts, compute the number of ints in the difference
        sq = (b * b - Decimal(4)*c).sqrt()
        right = int(( -b + sq )/Decimal(2))
        left = ((-b - sq)/Decimal(2)).to_integral_value(rounding=ROUND_CEILING)
        
        if lower_intercepts is None:
            to_add += max(right - int(left) + 1, 0)
        else:
            to_add += right - lower_intercepts[1] + 1
            to_add += lower_intercepts[0] - int(left) + 1
    tot += to_add
    if to_add:
        min_y = min(y, min_y)
        max_y = max(y, max_y)
    
print(tot, min_y, max_y)
