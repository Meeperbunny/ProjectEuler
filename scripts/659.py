# n = 100
n = 10_000_000
done = set([1])
ans = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    to_add = None
    # if len(ans[i]) == 2:
    #     continue
    if not len(ans[i]):
        to_add = (i * i * 4 + 1)
    else:
        to_add = (i * i * 4 + 1)
        for e in ans[i]:
            while to_add % e == 0:
                to_add //= e
    comp = to_add - i
    if to_add in done:
        continue
    else:
        done.add(to_add)
    for k in range(0, n + 1, to_add):
        if (k + i <= n):
            ans[k + i].append(to_add)
        if (k + comp <= n):
            ans[k + comp].append(to_add)
    # print(ans)
tot = 0
for e in ans:
    if len(e):
        tot += max(e)
tot