from tqdm import *

pnt_count = 2_500

def gen():
    s = 290797
    m = 50515093
    for _ in range(pnt_count):
        s = s * s
        s %= m
        f = s % 2000 - 1000
        s = s * s
        s %= m
        yield (f, s % 2000 - 1000)

pnts = list(set(gen()))

# For each point and every other point, get the slope and intercept

from math import gcd
from fractions import *
from collections import Counter

lines = {} # Takes slope as the key (None for vertical), and stores a list of intercepts.

for i, p_1 in tqdm(enumerate(pnts)):
    for p_2 in pnts[i+1:]:
        # Get slope and intercept
        dy, dx = p_1[1] - p_2[1], p_1[0] - p_2[0]
        slope = None
        if dx != 0:
            g = gcd(dy, dx)
            slope = Fraction(dy // g, dx // g)
        # If slope is none just store the x intercept. Otherwise, store the y intecept
        inter = None
        if slope == None:
            inter = p_1[0]
            if None not in lines:
                lines[None] = Counter()
            lines[slope][inter] += 1
        else:
            inter = Fraction(p_1[1]) - slope * Fraction(p_1[0])
            if slope.as_integer_ratio() not in lines:
                lines[slope.as_integer_ratio()] = Counter()
            lines[slope.as_integer_ratio()][inter.as_integer_ratio()] += 1

# Get distinct line count
distinct_line_count = len(pnts) * (len(pnts) - 1) // 2
for c in lines.values():
    for _, cnt in c.items():
        distinct_line_count -= cnt - 1

# Get the max intersection
max_intersections = distinct_line_count * (distinct_line_count - 1)
# Lines with the same slope will never intersect with eachother
for c in lines.values():
    cl = len(c)
    max_intersections -= cl * (cl - 1)

print(max_intersections)

