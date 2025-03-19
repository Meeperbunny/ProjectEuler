from math import sin, cos, pi
def rotate_vec(v, angle):
    return (cos(angle) * v[0] - sin(angle) * v[1], sin(angle) * v[0] + cos(angle) * v[1])
def dot(u, v):
    return u[0] * v[0] + u[1] * v[1]

def l_proj(v):
    left_vec = (cos(5 * pi / 6), sin(5 * pi / 6))
    s = dot(left_vec, v)
    # print("MAG", s)
    m = left_vec[0] * s, left_vec[1] * s
    return (m[0] * m[0] + m[1] * m[1])**0.5

def find_min_size(n, i):
    br_vec = (n, 0)
    tl_vec = (i / 2, i * 3**0.5 / 2)
    t_vec = (tl_vec[0] - br_vec[0], tl_vec[1] - br_vec[1])
    start = (0, 0)
    min_height = 0
    max_left = 0
    # print(t_vec)
    for i in range(6):
        # start is current point
        min_height = min(min_height, start[1])
        max_left = max(max_left, l_proj(start))
        # print("ST", start, min_height, max_left)
        start = (start[0] + t_vec[0], start[1] + t_vec[1])
        t_vec = rotate_vec(t_vec, pi * 1/3)
    leftmost = round(max_left / (3**0.5/2))
    lowest = round(min_height / (3**0.5/2))
    # print(leftmost, lowest)
    return int(abs(leftmost) + abs(lowest))
find_min_size(3, 2)

from tqdm import tqdm
# N = 12345
# T = 0
# r_cnts = 0
# t_cnts = 0
# d_cnts = 0
# m_cnts = [0] * (N + 1)
# for bl in tqdm(range(1, N + 1)):
#     d_cnts += m_cnts[bl]
#     t_cnts += d_cnts
#     r_cnts += t_cnts
#     for i in range(1, bl + 1):
#         min_size = find_min_size(bl, i)
#         if min_size <= N:
#             m_cnts[min_size] += 1
#     T += r_cnts
# print(T)

N = 12345
T = 0
r_cnts = 0
t_cnts = 0
d_cnts = 0
m_cnts = [0] * (N + 1)
for bl in tqdm(range(1, N + 1)):
    d_cnts += m_cnts[bl]
    t_cnts += d_cnts
    r_cnts += t_cnts
    min_size = bl * 3
    # Min size is always just bl * 3
    if min_size <= N:
        m_cnts[min_size] += bl
    T += r_cnts
print(T)