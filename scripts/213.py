from decimal import *

size = 10
steps = 5

def step(grid):
    new_grid = [[Decimal(0) for _ in range(size)] for _ in range(size)]
    for y in range(size):
        for x in range(size):
            to_dist = []
            curr = grid[y][x]
            if x > 0:
                to_dist.append((y, x - 1))
            if y > 0:
                to_dist.append((y - 1, x))
            if x < size - 1:
                to_dist.append((y, x + 1))
            if y < size - 1:
                to_dist.append((y + 1, x))
            sz = len(to_dist)
            for el in to_dist:
                new_grid[el[0]][el[1]] += curr / Decimal(sz)
    return new_grid

def get_prob(x, y):
    print(f"Getting {x} {y}")
    base = [[Decimal(0) for _ in range(size)] for _ in range(size)]
    base[y][x] = Decimal(1)
    for s in range(steps):
        base = step(base)
    return base

probs = [[get_prob(i, j) for j in range(size)] for i in range(size)]

ev = Decimal(0)
for i in range(size):
    for q in range(size):
        base_p = 1
        for y in range(size):
            for x in range(size):
                base_p *= Decimal(1) - probs[y][x][i][q]
        print(round(base_p, 5), end=' ')
        ev += base_p
    print()
print(ev)