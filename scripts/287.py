def f(x, y, N):
    return (x - 2**(N - 1))**2 + (y - 2**(N - 1))**2 <= 2**(2 * N - 2)
N = 24
def describe(x1, y1, x2, y2, z):
    # If four coner are same
    if not z and len(set(
        f(x, y, N) for (x, y) in [
            (x1, y1), (x2 - 1, y1), (x1, y2 - 1), (x2 - 1, y2 - 1)
        ]
    )) == 1:
        return 2
    else:
        mx = (x2 - x1) // 2 + x1
        my = (y2 - y1) // 2 + y1
        return 1 + describe(x1, y1, mx, my, False) + \
                    + describe(x1, my, mx, y2, False) + \
                    + describe(mx, my, x2, y2, False) + \
                    + describe(mx, y1, x2, my, False)
print(describe(0, 0, 2**N, 2**N, True))