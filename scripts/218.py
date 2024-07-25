maxn = int(1e8)
sqrc = 1
notsp = 0
while sqrc * sqrc <= maxn:
    m = 1
    c = sqrc * sqrc
    while m * m < c:
        nsq = c - m * m
#         print(c, m, nsq)
        if int(nsq**0.5) == nsq**0.5:
            n = int(nsq**0.5)
            a = m * m - n * n
            b = 2 * m * n
            if (a * b // 2) % 84 != 0:
                notsp += 1
#             print(a, b, c)
        m += 1
    sqrc += 1
print(notsp)