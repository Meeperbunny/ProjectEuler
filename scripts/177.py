# from math import sin, cos, asin, pi, isclose
# def is_integer_angle(a):
#     return isclose(round(a), a, abs_tol=1e-9)
# def a_to_r(a):
#     return a / 180 * pi
# def r_to_a(a):
#     return a / pi * 180 
# AC = 9
# from decimal import Decimal
# from tqdm import trange
# def get_angles(a1, a2, c1, c2):
#     # Convert to rads
#     a1, a2, c1, c2 = a_to_r(a1), a_to_r(a2), a_to_r(c1), a_to_r(c2)
#     c_bl = pi - a2 - c1
#     c_ul = pi - c_bl
#     d2 = pi - a1 - c_ul
#     c_ur = c_bl
#     c_br = c_ul
#     b1 = pi - c2 - c_br
#     # print(r_to_a(b1), r_to_a(c2), r_to_a(c_br))
#     a_o = 1
#     c_o = a_o / sin(c1) * sin(a2)
#     d_o = a_o / sin(d2) * sin(a1)
#     # print(b1, c2)
#     b_o = c_o / sin(b1) * sin(c2)
#     d_b = (b_o**2 + d_o**2 - 2*b_o*d_o*cos(c_ur))**0.5
#     asin_value = min(max(b_o / d_b * sin(c_ur), 0), 1)
#     d1 = asin(asin_value)
#     b2 = pi - (c_ur + d1)
#     # Get side lengths for similarity
#     d_b = (d_b)
#     d_a = (a_o / sin(d2) * sin(c_ul))
#     a_c = (a_o / sin(c1) * sin(c_bl))
#     c_b = (c_o / sin(b1) * sin(c_br))
#     sides = (a_c, c_b, d_b, d_a)
#     return (r_to_a(b1), r_to_a(b2), r_to_a(d1), r_to_a(d2)), (*sides, max(sides))
# get_angles(45, 45, 45, 45)
# ANS = 0
# S = set()
# for a1 in range(1, 180):
#     for a2 in range(1, 180 - a1):
#         for c1 in range(1, 180 - a1 - a2):
#             for c2 in range(1, 180 - c1 - a2):
#                 # print(a1, a2, c1, c2)
#                 angles, sides = get_angles(a1, a2, c1, c2)
#                 # if a1 == 1 and a2 == 89 and c1 == 89:
#                 #     print(angles, tuple(is_integer_angle(a) for a in angles))
#                 if min(is_integer_angle(a) for a in angles) == True:
#                     # A = round(a1 + a2)
#                     # B = round(angles[0] + angles[1])
#                     # C = round(c1 + c2 )
#                     # D = round(angles[2] + angles[3])
#                     S.add(sides)
#                     ANS += 1
# print(ANS, len(S))

# def cyclic_shift(T):
#     return list((tuple(T[(i + q) % 4] for q in range(4))) for i in range(4))
# C = 0
# rounded_s = {}
# for el in S:
#     rounded_s[tuple(round(e / el[4], AC) for e in el[0:4])] = el
# # print(rounded_s)
# from collections import Counter
# rmcnt = Counter()
# while len(S):
#     C += 1
#     e = S.pop()
#     sides, mside = e[0:4], e[4]
#     sides = tuple(round(e / mside, AC) for e in sides)
#     r_sides = tuple(reversed(sides))
#     to_remove = cyclic_shift(sides) + cyclic_shift(r_sides)
#     # print("EE", e, to_remove)
#     rmed = 0
#     for e in to_remove:
#         if e in rounded_s:
#             # print(e, rounded_s[e], rounded_s[e] in S)
#             if rounded_s[e] in S:
#                 S.remove(rounded_s[e])
#                 rmed += 1
#     rmcnt[rmed] += 1
# print(C, rmcnt)


from math import sin, cos, asin, pi, isclose
def is_integer_angle(a):
    return isclose(round(a), a, abs_tol=1e-3)
def a_to_r(a):
    return a / 180 * pi
def r_to_a(a):
    return a / pi * 180 
AC = 9
from decimal import Decimal
from tqdm import trange
def get_angles(a1, a2, c1, c2):
    # Convert to rads
    a1, a2, c1, c2 = a_to_r(a1), a_to_r(a2), a_to_r(c1), a_to_r(c2)
    c_bl = pi - a2 - c1
    c_ul = pi - c_bl
    d2 = pi - a1 - c_ul
    c_ur = c_bl
    c_br = c_ul
    b1 = pi - c2 - c_br
    # print(r_to_a(b1), r_to_a(c2), r_to_a(c_br))
    a_o = 1
    c_o = a_o / sin(c1) * sin(a2)
    d_o = a_o / sin(d2) * sin(a1)
    # print(b1, c2)
    b_o = c_o / sin(b1) * sin(c2)
    d_b = (b_o**2 + d_o**2 - 2*b_o*d_o*cos(c_ur))**0.5
    asin_value = min(max(b_o / d_b * sin(c_ur), 0), 1)
    d1 = asin(asin_value)
    b2 = pi - (c_ur + d1)

    return (r_to_a(b1), r_to_a(b2), r_to_a(d1), r_to_a(d2))
ANS = 0
S = set()
for a1 in trange(1, 180):
    for a2 in range(1, 180):
        for c1 in range(1, 180):
            for c2 in range(1, 180):
                if a2 + c1 >= 180:
                    continue
                if a1 + a2 + c1 >= 180:
                    continue
                if a2 + c1 + c2 >= 180:
                    continue
                # print(a1, a2, c1, c2)
                angles = get_angles(a1, a2, c1, c2)
                # if a1 == 1 and a2 == 89 and c1 == 89:
                #     print(angles, tuple(is_integer_angle(a) for a in angles))
                if min(is_integer_angle(a) for a in angles) == True:
                    t = tuple((a1, a2, c1, c2, angles[0], angles[1], angles[2], angles[3]))
                    t = tuple(round(e) for e in t)
                    S.add(t)
                ANS += 1
print(ANS, len(S))

def cyclic_shift(T):
    l = []
    for i in range(4):
        t = tuple(T[(i * 2 + q) % 8] for q in range(8))
        l.append(t)
    return l
C = 0
from collections import Counter
rmcnt = Counter()
while len(S):
    C += 1
    angles = S.pop()
    r_angles = tuple(reversed(angles))
    to_remove = cyclic_shift(angles) + cyclic_shift(r_angles)
    rmed = 0
    for e in to_remove:
        if e in S:
            S.remove(e)
            rmed += 1
    rmcnt[rmed] += 1
print(C, rmcnt)