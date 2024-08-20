from collections import Counter

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

def construct(b, w):
    n = b + w
    # Ways[num][# of num][target] is # of ways for # of num to add up to target in non-decreasing list  
    ways = [[[0 for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(n + 1)]
    for num in range(1, n + 1):
        ways[num][0][0] = 1
        table = [[[0 for _ in range(num + 1)] for _ in range(n + 1)] for _ in range(n + 1)]
        table[0][0][0] = 1
        for n_cnt in range(0, n):
            for total in range(0, n + 1):
                for l_inc in range(0, num + 1):
                    for to_add in range(l_inc, num + 1):
                        if total + to_add <= n:
                            table[n_cnt + 1][total + to_add][to_add] += table[n_cnt][total][l_inc]
            # After finishing n_cnt iteration, n_cnt + 1 is done.
            # for tar in range(0, n + 1):
            #     for l_inc in range(0, num + 1):
            #         ways[num][n_cnt + 1][tar] += table[n_cnt + 1][tar][l_inc]
            for tar in range(0, n + 1):
                # print(table[n_cnt + 1][tar])
                # print(num, n_cnt + 1, tar, sum(table[n_cnt + 1][tar]))
                # for l_inc in range(0, num + 1):
                ways[num][n_cnt + 1][tar] += sum(table[n_cnt + 1][tar])
            # print(ways[num][n_cnt + 1])
    return ways

def calc(part, b, w):
    p = min(b, w)
    cnts = Counter(part)
    t = [0 for _ in range(p + 1)]
    t[p] = 1
    for e in cnts:
        t_n = [0 for _ in range(p + 1)]
        ways = c[e][cnts[e]]
        for i in range(0, p + 1):
            for j in range(0, i + 1):
                # At i, remove j.
                t_n[i - j] += t[i] * ways[j]
        t = t_n
    return t[0]

b, w = 60, 40
print("Constructing")
c = construct(b, w)
print("Construction Done")
ways = 0
i = 0
for part in mckay(b + w):
    if i % (190634173 // 1000) == 0:
        print(i / 190634173)
    i += 1
    ways += calc(part, b, w)
    # print(part, calc(part, b, w))
print(ways)