import math
from itertools import combinations
from tqdm import tqdm

# Global constant and helper
x = 1
TAN = lambda angle: round(math.tan(angle), 3)

# Precomputed allowed slopes for each label.
AXIS_SLOPES = {
    "CO": (0, None, TAN(math.pi/6), TAN(math.pi/3), TAN(2*math.pi/3), TAN(5*math.pi/6)),
    "C":  (None, TAN(math.pi/6), TAN(5*math.pi/6)),
    "TR": (TAN(math.pi/6), TAN(2*math.pi/3)),
    "BO": (0, None),
    "TL": (TAN(5*math.pi/6), TAN(math.pi/3)),
}

def are_same_axis(a, b):
    """
    Returns True if two points (each as ((x, y), label)) share an allowed axis.
    In the vertical case (x difference near 0), we check b’s label.
    Otherwise, we compute the slope (via atan→tan rounded to 3 decimals)
    and see if it is in the allowed set for a’s label.
    """
    (x_a, y_a), label_a = a
    (x_b, y_b), label_b = b
    if abs(x_a - x_b) < 1e-3:
        return label_b in ("CO", "C", "BO")
    slope = (y_a - y_b) / (x_a - x_b)
    tan_val = round(math.tan(math.atan(slope)), 3)
    return tan_val in AXIS_SLOPES.get(label_a, ())

def is_degenerate_triangle(a, b, c, tol=1e-6):
    """
    Uses the area formula to decide if the triangle defined by a, b, c (each as (x, y))
    is degenerate (i.e. nearly collinear or with coincident vertices).
    """
    if a == b or b == c or a == c:
        return True
    area = abs(a[0]*(b[1]-c[1]) + b[0]*(c[1]-a[1]) + c[0]*(a[1]-b[1])) / 2
    return area < tol

def gen_triangle(center, reversed=False):
    """
    Given a center point, returns a set of points (with labels) for a triangle.
    The triangle includes the center ("C") and six points around it, with orientation
    flipped if reversed==True.
    """
    R = math.pi if reversed else 0
    pts = { (center, "C") }
    for mult, offset, label in [
            (1, math.pi/6,    "TR"),
            (1, 5*math.pi/6,  "TL"),
            (1, 9*math.pi/6,  "BO"),
            (2, 3*math.pi/6,  "CO"),
            (2, 7*math.pi/6,  "CO"),
            (2, 11*math.pi/6, "CO"),
        ]:
        angle = R + offset
        pt = (center[0] + mult * x * math.cos(angle),
              center[1] + mult * x * math.sin(angle))
        pts.add((pt, label))
    return pts

def gen_points(k):
    """
    Generates points (each as ((x, y), label)) arranged in a spiral of triangles.
    Duplicate coordinates (after rounding) are filtered out.
    The inner loop has been rewritten to mimic the original offset logic.
    """
    points = set()
    seen = set()  # To avoid duplicate (rounded) coordinates
    i, increment, start = 0, 1, 0
    base = 0  # Horizontal base offset (s0 in the original)
    
    while True:
        if i == k - 1:
            increment = -1
        # Loop over positions in this row: j runs from 1 to i+1.
        for j in range(1, i + 2):
            # Original: for q in range(start+1, start+i+2) with an offset_counter that increments every even j.
            q = start + j
            offset = (j - 1) // 2
            # Compute radius following the original: 2 * x * (2*start + q + offset)
            radius = 2 * x * (2 * start + q + offset)
            center = (base + radius * math.cos(math.pi/6),
                      radius * math.sin(math.pi/6))
            # Alternate triangle orientation based on parity of j.
            tri = gen_triangle(center, reversed=(j % 2 == 0))
            for pt, label in tri:
                rounded = (round(pt[0], 2), round(pt[1], 2))
                if rounded not in seen:
                    seen.add(rounded)
                    points.add(((pt[0], pt[1]), label))
        base -= 2 * x * math.sqrt(3)
        i += increment
        if increment == -1:
            start += 1
        if i < 0:
            break
    return points

# Generate our points.
P = list(gen_points(36))
n = len(P)
total_triangles = math.comb(n, 3)

# Cache repeated axis comparisons.
axis_cache = {}
def axis_pair(i, j):
    key = (i, j)
    if key not in axis_cache:
        axis_cache[key] = are_same_axis(P[i], P[j])
    return axis_cache[key]

# Count valid triangles.
count = 0
for i, j, k in tqdm(combinations(range(n), 3), total=total_triangles):
    # Check non-degeneracy (via area) and that all three pairs share an allowed axis.
    if (not is_degenerate_triangle(P[i][0], P[j][0], P[k][0]) and
        axis_pair(i, j) and axis_pair(i, k) and axis_pair(j, k)):
        count += 1

print(count)
