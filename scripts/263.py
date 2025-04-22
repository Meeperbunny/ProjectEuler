from random import randint
def miller_rabin(n, k=5):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    
    y = 0
    for _ in range(k):
        a = randint(2, n - 2)
        x = pow(a, d, n)
        for _ in range(s):
            y = pow(x, 2, n)
            if y == 1 and x != 1 and x != n - 1:
                return False
            x = y
        if y != 1:
            return False
    return True
from functools import lru_cache

@lru_cache
def divs(n):
    f = []
    b = []
    for i in range(1, n):
        if i * i > n:
            break
        if n % i == 0:
            f.append(i)
            if i * i != n:
                b.append(n // i)
    return list(f) + list(reversed(b))

@lru_cache
def isgood(n):
    csum = 0
    for e in divs(n):
        if e <= csum + 1:
            csum += e
        else:
            return False
    return True
b_num = 10
C = 4
T = 0
bb = 1
tar = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1]
while C:
    if bb == 1_000_000:
        print(b_num)
        bb = 0
    bb += 1
    # if b_num > M:
    #     break
    # print(b_num)
    isg = True
    if isg:
        i = 0
        for e in range(-9, 9 + 1, 2):
            if tar[i] != miller_rabin(b_num + e):
                isg = False
                break
            i += 1
        if isg:
            # print("SPAIR", b_num)
            for t in [-8, -4, 0, 4, 8]:
                # print('\t', b_num + t, isgood(b_num + t))
                if not isgood(b_num + t):
                    isg = False
                    break
            if isg:
                print("PARADISE", b_num)
                C -= 1
                T += b_num
    b_num += 2
print(T)