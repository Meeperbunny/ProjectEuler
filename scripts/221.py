from heapq import *
L = []
N = 150_000
a = 1
lower_a = 1
while True:
    sq = a * a + 1
    while len(L) >= N and a * (a + lower_a) * (a + lower_a + 1) > -L[0] and lower_a <= a:
        lower_a += 1
    if lower_a == a + 1:
        break
    for i in range(a, lower_a - 1, -1):
        if sq % i == 0:
            o = sq // i
            j = o - i
            a, b, c = a, a + i, a + i + j
            heappush(L, -a * b * c)
            while len(L) > N:
                heappop(L)
    a += 1
print(-L[0])