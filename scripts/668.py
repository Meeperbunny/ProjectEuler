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

def ans_f(n):
    cnt = 0
    isbad = set()
    mcheck = n // 100000
    for i in range(2, n + 1):
        if mcheck and i % mcheck == 0:
            print(i / n)
        if (miller_rabin(i)):
            max_val = min(n, i * i)
            min_val = i
            cnt += (max_val - min_val + i) // i
    return n - cnt

n = 10**10
print(ans_f(n))