from heapq import *
from tqdm import trange
N = 10**9
min_cost = [0]
for i in trange(1, N):
    # Get min cost
    mc = heappop(min_cost)
    heappush(min_cost, mc + 1)
    heappush(min_cost, mc + 4)
len(min_cost), sum(min_cost)