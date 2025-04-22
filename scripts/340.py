from sys import setrecursionlimit
setrecursionlimit(10_000)

a, b, c = 21**7, 7**21, 12**7
def F(n):
    global a, b, c
    if n > b:
        return n - c
    return F(a + F(a + F(a + F(a + n))))

def tri(n): return (n * (n + 1) // 2)
a * 4 - c * 3
a, b, c
cind = b
iv = F(b)
T = 0
lk = 1
i = 0
while cind >= 0:
    i += 1
    if i > lk:
        lk = lk * 2
        print(i, cind)
    lower = max(cind - a, -1)
    len = cind - lower
    inc = a * 4 - c * 3
    T += iv * len - tri(len - 1)
    iv += inc - len
    cind = lower
print(T, T % 10**9)