def contains(triangle, point):
    """Checks if triangle contains the point (exclusive of edge)"""
    A, B, C = triangle
    P = point
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    cp1 = cross(A, B, P)
    cp2 = cross(B, C, P)
    cp3 = cross(C, A, P)
    if cp1 == 0 or cp2 == 0 or cp3 == 0:
        return False
    if (cp1 > 0 and cp2 > 0 and cp3 > 0) or (cp1 < 0 and cp2 < 0 and cp3 < 0):
        return True
    return False