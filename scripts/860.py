from collections import Counter
def F(n):
    a = Counter([0])
    b = Counter([0])
    new_b = Counter()
    for e in b:
        new_b[e + 4] += b[e]
        new_b[e + 1] += b[e]
        new_b[e - 1] += b[e]
        new_b[e - 4] += b[e]
    b = new_b

    while n:
        print(n)
        if n & 1:
            new_a = Counter()
            for e_a in a:
                for e_b in b:
                    new_a[e_a + e_b] += a[e_a] * b[e_b]
                    new_a[e_a + e_b] %= 989898989
            a = new_a
            n -= 1
        else:
            new_b = Counter()
            for e_f in b:
                for e_s in b:
                    new_b[e_f + e_s] += b[e_f] * b[e_s]
                    new_b[e_f + e_s] %= 989898989
            b = new_b
            n >>= 1
    return a[0]
print(F(9898))