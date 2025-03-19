def isprime(k):
    for i in range(2, k):
        if i * i > k:
            break
        if k % i == 0:
            return False
    return True

def last_digits(p):
    b = 1
    digits = []
    for i in range(p - 1):
        b *= 10
        c = b // p
        digits.append(c)
        b -= c * p
    return digits

def last_digits(p):
    b = 1
    digits = []
    s = 0
    for i in range(p - 1):
        b *= 10
        c = b // p
        if i < 10 or i > p - 10:
            digits.append(c)
        s += c
        b -= c * p
    return digits, s

for k in range(720009891, 729909891 + 1):
    if k % 100000 != 9891:
        continue
    if isprime(k):
        print("Checking", k)
        dl, ds = last_digits(k)
        if dl[-5:] == [5, 6, 7, 8, 9]:
            print(dl, ds)