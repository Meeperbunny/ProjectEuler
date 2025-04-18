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
ma = 5 * 10**15
nums = []
k = 1
C = 0
while True:
    if miller_rabin(k**2 + (k+1)**2):
        b = (k) * (k + 1) + 1
        dub = b * 2 - 2
        x, y = b * k + b, b * k
        num = (x**4 - y**4) / (x**3 + y**3)
        if num > ma:
            print("Done at k = {}".format(k))
            break
        C += 1
    k += 1
print("Answer: {}".format(C))