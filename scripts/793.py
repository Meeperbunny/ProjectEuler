def ans(n):
    s = [290797]
    while len(s) < n:
        s.append(s[-1] * s[-1] % 50515093)
    s.sort()
    # Binary search. For each s, check how many are above m. Our goal should be to always be less than or eq to ((n) * (n - 1) - 1) // 2.
    l = -1
    m = 5000000000000000
    tar = ((n * (n - 1)) // 2  - 1) // 2
    while m >= 1:
        print(m)
        while True:
            cnt = 0
            n_med = l + m
            # Iterate through, at each el see what count is
            for i in range(n):
                ind_c = -1
                inc = n
                while inc >= 1:
                    while True:
                        n_lower = ind_c + inc
                        if n_lower >= i:
                            break
                        if s[n_lower] * s[i] <= n_med:
                            ind_c += inc
                        else:
                            break
                    inc //= 2
                # print(i, n_med, ind_c + 1)
                cnt += ind_c + 1

            # print(n_med, cnt, tar)
            
            if cnt <= tar:
                l = n_med
            else:
                break
        m //= 2
    return l + 1
print(ans(1000003))