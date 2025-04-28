from concurrent.futures import ProcessPoolExecutor
from multiprocessing import cpu_count
from tqdm import tqdm
import random

def random_permutation(n):
    return random.sample(range(1, n + 1), n)

def trial(n):
    p = random_permutation(n)
    m = 0
    i = 0
    C = 0
    for e in p:
        i |= (1 << e)
        C += 1 - ((i >> (e - 1)) & 1) - ((i >> (e + 1)) & 1)
        m = max(C, m)
    return m

def worker(args):
    n, trials = args
    c = 0
    for _ in range(trials):
        c += trial(n)
    return c

# 11.4928456648

if __name__ == '__main__':
    n = 40
    T = 5 * 10**9
    workers = cpu_count()
    base, rem = divmod(T, workers)
    chunks = [base + (1 if i < rem else 0) for i in range(workers)]
    args = [(n, c) for c in chunks]

    total = 0
    with ProcessPoolExecutor() as exe:
        for c in tqdm(exe.map(worker, args), total=workers):
            total += c

    print(total, T, total / T)
