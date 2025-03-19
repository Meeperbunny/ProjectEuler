# %%
DIGITS = 16
N = 10**DIGITS

# %%
import unittest

def mckay(n):
    """
    Integer partitions of n, in reverse lexicographic order.
    Note that the generated output consists of the same list object,
    repeated the correct number of times; the caller must leave this
    list unchanged, and must make a copy of any partition that is
    intended to last longer than the next call into the generator.
    The algorithm follows Knuth v4 fasc3 p38 in rough outline.
    """
    if n == 0:
        yield []
    if n <= 0:
        return
    partition = [n]
    last_nonunit = (n > 1) - 1
    while True:
        yield partition
        if last_nonunit < 0:
            return
        if partition[last_nonunit] == 2:
            partition[last_nonunit] = 1
            partition.append(1)
            last_nonunit -= 1
            continue
        replacement = partition[last_nonunit] - 1
        total_replaced = replacement + len(partition) - last_nonunit
        reps,rest = divmod(total_replaced,replacement)
        partition[last_nonunit:] = reps*[replacement]
        if rest:
            partition.append(rest)
        last_nonunit = len(partition) - (partition[-1]==1) - 1

def integer_partition(n):
    return [e.copy() for e in mckay(n)]
# print(len(integer_partition(80)))

# %%
parts = integer_partition(DIGITS)
parts = [e + [0] * (10 - len(e)) for e in parts if len(e) <= 10]

# %%
from itertools import permutations

# %%
from tqdm import tqdm

# %%
perm_set = set()
for p in tqdm(parts):
    perm_set.update(set(permutations(p)))

# %%
def num_to_list(i: int):
    l = [0 for _ in range(10)]
    for c in str(i):
        l[ord(c) - ord('0')] += 1
    return l

# %%
def is_eq(base_num, l):
    for i in range(1, 10):
        if l[i] != base_num[i]:
            return False
    return l[0] <= base_num[0]

# %%
good_set = set()

for perm in tqdm(perm_set):
    # print(perm)
    # If all 0's or 1's, dont consider
    if perm[0] + perm[1] == DIGITS:
        continue
    k = 1
    while True:
        t = 0
        for i in range(0, 10):
            t += perm[i] * i**k
        if t > N + 3:
            break
        # Turn sum into num + 1, num - 1. Check if it is eq to original perm. If so, add the num into the list for each.
        lower = num_to_list(t - 1)
        upper = num_to_list(t + 1)

        if (is_eq(perm, lower)):
            good_set.add(t - 1)
        if (is_eq(perm, upper)):
            good_set.add(t + 1)
        
        k += 1


# %%
good_set

# %%
sum(good_set)


