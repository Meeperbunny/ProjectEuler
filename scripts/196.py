from random import randint
def miller_rabin(n, k=5):
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

def get_row(n):
    print("Starting a row")
    ret = [(1 if miller_rabin(n * (n - 1) // 2 + 1 + i) else 0) for i in range(n)]
    print("Done getting row")
    return ret

def cnt(n):
    row = [get_row(n - 2), get_row(n - 1), get_row(n), get_row(n + 1), get_row(n + 2)]
#     for r in row:
#         print(r)
    for i in range(len(row[1])):
        if (row[1][i]):
            cnt = 1
            for x in range(-1, 2):
                for y in range(-1, 2):
                    n_c = 1 + y
                    n_r = i + x
                    if ((x != 0 or y != 0) and n_r >= 0 and n_r < len(row[n_c])):
                        if row[n_c][n_r]:
                            cnt += 1
            if cnt >= 3:
                for x in range(-1, 2):
                    n_c = 2
                    n_r = i + x
                    if (n_r >= 0 and n_r < len(row[n_c])):
                        if row[n_c][n_r]:
                            row[n_c][n_r] = 2
    print("Done With Row 1")
    for i in range(len(row[2])):
        if (row[2][i]):
            cnt = 1
            for x in range(-1, 2):
                for y in range(-1, 2):
                    n_c = 2 + y
                    n_r = i + x
                    if ((x != 0 or y != 0) and n_r >= 0 and n_r < len(row[n_c])):
                        if row[n_c][n_r]:
                            cnt += 1
            if cnt >= 3:
                for x in range(-1, 2):
                    n_c = 2
                    n_r = i + x
                    if (n_r >= 0 and n_r < len(row[n_c])):
                        if row[n_c][n_r]:
                            row[n_c][n_r] = 2
    print("Done With Row 2")
                            
    for i in range(len(row[3])):
        if (row[3][i]):
            cnt = 1
            for x in range(-1, 2):
                for y in range(-1, 2):
                    n_c = 3 + y
                    n_r = i + x
                    if ((x != 0 or y != 0) and n_r >= 0 and n_r < len(row[n_c])):
                        if row[n_c][n_r]:
                            cnt += 1
            if cnt >= 3:
                for x in range(-1, 2):
                    n_c = 2
                    n_r = i + x
                    if (n_r >= 0 and n_r < len(row[n_c])):
                        if row[n_c][n_r]:
                            row[n_c][n_r] = 2
    print("Done With Row 3")
#     for r in row:
#         print(r)
    t = 0
    for i in range(n):
        if row[2][i] == 2:
            t += n * (n - 1) // 2 + 1 + i
    print("Total Done")
    return t

# print(cnt(10_000))
print(cnt(5678027) + cnt(7208785))