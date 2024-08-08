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

n = 10**12

print("Finding Relevant Numbers")

# Find all numbers of the form 2^a * 3^b * 5^c.
nums = set([1])
for p in [2, 3, 5]:
    powers = []
    i = 1
    while i <= n:
        powers.append(i)
        i *= p
    n_nums = set()
    for e1 in nums:
        for e2 in powers:
            if e1 * e2 <= n:
                n_nums.add(e1 * e2)
    nums = n_nums
len(nums)

print("Checking if Prime")

# For each el, check if e + 1 is prime. If so, then can mult at least once.
canreach = set([1])
for qq, e in enumerate(nums):
    print(qq / len(nums))
    if e <= 5 or e + 1 > n:
        continue
    if miller_rabin(e + 1):
        # print(e + 1)
        n_nums = set()
        for e1 in canreach:
            if e1 * (e + 1) <= n:
                n_nums.add(e1 * (e + 1))
        for e in n_nums:
            canreach.add(e)


print("Finding Rest of Numbers", len(canreach))

# Find all numbers of the form 2^a * 3^b * 5^c.
nums = set(canreach)
for p in [2, 3, 5]:
    print("On", p, len(canreach))
    powers = []
    i = 1
    while i <= n:
        powers.append(i)
        i *= p
    n_nums = set()
    for qz, e2 in enumerate(powers):
        print(e2, qz / len(powers))
        for e1 in nums:
            if e1 * e2 <= n:
                n_nums.add(e1 * e2)
    nums = n_nums

print(sum(nums) % 4294967296)