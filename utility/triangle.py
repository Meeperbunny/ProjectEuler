def contains(triangle, point):
    A, B, C = triangle
    v0 = (C[0] - A[0], C[1] - A[1])
    v1 = (B[0] - A[0], B[1] - A[1])
    v2 = (point[0] - A[0], point[1] - A[1])
    dot00 = v0[0] * v0[0] + v0[1] * v0[1]
    dot01 = v0[0] * v1[0] + v0[1] * v1[1]
    dot02 = v0[0] * v2[0] + v0[1] * v2[1]
    dot11 = v1[0] * v1[0] + v1[1] * v1[1]
    dot12 = v1[0] * v2[0] + v1[1] * v2[1]
    denom = dot00 * dot11 - dot01 * dot01
    if denom == 0:
        return False
    # Compute barycentric coordinates using the dot products
    inv_denom = 1 / denom
    u = (dot11 * dot02 - dot01 * dot12) * inv_denom
    v = (dot00 * dot12 - dot01 * dot02) * inv_denom
    # Check if point is inside the triangle: THIS IS INCLUSIVE. For exclusive do !=?
    return (u >= 0) and (v >= 0) and (u + v <= 1)