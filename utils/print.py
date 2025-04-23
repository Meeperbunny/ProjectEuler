def print_aligned(matrix):
    col_widths = [max(len(str(matrix[row][col])) for row in range(len(matrix))) 
                  for col in range(len(matrix[0]))]

    for row in matrix:
        print(" ".join(f"{num:>{col_widths[i]}}" for i, num in enumerate(row)))