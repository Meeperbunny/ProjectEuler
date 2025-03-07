def is_r(n):
    n_s = str(n)
    n_s = int(n_s[1:] + n_s[0])
    return n_s % n == 0

for i in range(1000000000000, 2000000000000):
    if is_r(i):
        print(i)