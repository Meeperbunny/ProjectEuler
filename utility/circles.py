# https://en.wikipedia.org/wiki/Descartes%27_theorem#:~:text=In%20geometry%2C%20Descartes'%20theorem%20states,three%20given%2C%20mutually%20tangent%20circles.
# k_i is the curvature, k_i = 1 / r_i
def find_internal_curvature(k_1, k_2, k_3):
    first = k_1 + k_2 + k_3
    second = k_1 * k_2 + k_2 * k_3 + k_3 * k_1
    k_ans_1, k_ans_2 = first + 2 * second**0.5, first - 2 * second**0.5
    return k_ans_1 #k_ans_2 # Empirically don't use the second answer. Unsure when it is useful

# https://en.wikipedia.org/wiki/Descartes%27_theorem#:~:text=In%20geometry%2C%20Descartes'%20theorem%20states,three%20given%2C%20mutually%20tangent%20circles.
# k_i is the curvature, k_i = 1 / r_i
# P_1 is a tuple given in cartesian coordinates
def find_internal_circle(k_1, k_2, k_3, P_1, P_2, P_3):
    k_4 = find_internal_curvature(k_1, k_2, k_3)
    r = 1 / k_4
    # Converts cartesian to imaginary (x, y) -> x + iy
    z_1 = P_1[0] + P_1[1] * 1j
    z_2 = P_2[0] + P_2[1] * 1j
    z_3 = P_3[0] + P_3[1] * 1j
    first = z_1 * k_1 + z_2 * k_2 + z_3 * k_3
    second = k_1 * k_2 * z_1 * z_2 + k_2 * k_3 * z_2 * z_3 + k_1 * k_3 * z_1 * z_3
    z_ans_1 = (first + 2 * second**0.5) / k_4
    z_ans_2 = (first - 2 * second**0.5) / k_4
    p_1, p_2 = (z_ans_1.real, z_ans_1.imag), (z_ans_2.real, z_ans_2.imag)
    return p_1, r # Empirically don't use the second answer. Unsure when it is useful