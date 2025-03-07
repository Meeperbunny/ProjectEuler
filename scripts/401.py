maxn = int(1e15)
max_sq = int(maxn**0.5)
mod = int(1e9)
def sq_sum(n):
    return n * (n + 1) * (2 * n + 1) // 6
tot = 0
for i in range(1, max_sq + 1):
    if i % (max_sq // 100) == 0:
        a = i // (max_sq // 100)
        print("#" * a + '.' * (100 - a))
    # Definer lower part
    cnt = maxn // i
    lower = (maxn // i - i + 1) * (i * i)
    # Define upper part
#     print(cnt, i, sq_sum(cnt), sq_sum(i))
    upper = (sq_sum(cnt) - sq_sum(i))
#     print(i, lower, upper)
    tot += lower + upper
    tot %= mod
print(tot)