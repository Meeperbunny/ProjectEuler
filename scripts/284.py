md = 10_000
# md = 9
def trimmed(s):
    return s.lstrip('0')
def todec(s):
    num = 0
    for c in s:
        num *= 14
        if c in "ABCD":
            num += ord(c) - ord('A') + 10
        else:
            num += ord(c) - ord('0')
    return num
def b14(num, dd=9999999999):
    if num == 0:
        return '0'
    digits = "0123456789ABCD"
    result = ''
    while num > 0 and dd:
        dd -= 1
        result = digits[num % 14] + result
        num //= 14
    return result
ls = []
for i in range(1, 14):
    si = b14(i)
    if si == b14(i * i)[-len(si):]:
        ls.append((si, i))
        # print(i, b14(i), b14(i * i))
def expand(ls):
    isg = []
    for num, ni in ls:
        if len(num) >= md:
            continue
        for pre in range(0, 14):
            ta = b14(pre)
            nbnum = ta + num
            nni = pre * pow(14, len(num)) + ni
            if (nni**2 // pow(14, len(num))) % 14 == pre:
                isg.append((nbnum, nni))
    return isg
mds = 0
base = ls
goods = set()
while len(base):
    print(len(base), mds)
    for el, _ in base:
        goods.add(trimmed(el))
    base = expand(base)
    mds += 1
def b14dsum(s):
    T = 0
    for c in s:
        if c in "ABCD":
            T += ord(c) - ord('A') + 10
        else:
            T += ord(c) - ord('0')
    return T
# goods = {todec(e) for e, _ in goods if len(e) <= md}
T = 0
for e in goods:
    T += b14dsum(e)
print(T)