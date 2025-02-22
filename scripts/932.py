from math import log10
from tqdm import tqdm

isgood = set()
maxdigits = 16
isz = 1
isq = 10
for i in tqdm(range(1, int(10**(maxdigits//2)+1))):
# for i in tqdm(range(20, 22)):
    if i == isq:
        isz += 1
        isq *= 10
    # TRY LEFT
    for rs_digits in range(1, maxdigits - isz + 1):
        a, b, c = 1, 2 * i - 1, i * i - i * rs_digits
        m = b**2-4*a*c
        if (m>=0):
            e = int(((-b + (m)**0.5) / (2 * a)))
            if e >= 1 and int(log10(e)) + 1 == rs_digits and i * rs_digits + e == (i + e)**2:
                isgood.add(i * rs_digits + e)
            e = int(((-b - (m)**0.5) / (2 * a)))
            if e >= 1 and int(log10(e)) + 1 == rs_digits and i * rs_digits + e == (i + e)**2:
                isgood.add(i * rs_digits + e)
    # TRY RIGHT
    a, b, c = 1, 2 * i - isq, i**2 - i
    m = b**2-4*a*c
    if (m>=0):
        e = int(((-b + (m)**0.5) / (2 * a)))
        if e >= 1 and e * isq + i == (i + e)**2:
            isgood.add(e * isq + i)
        e = int(((-b - (m)**0.5) / (2 * a)))
        if e >= 1 and e * isq + i == (i + e)**2:
            isgood.add(e * isq + i)
print(isgood)
print(sum(isgood))