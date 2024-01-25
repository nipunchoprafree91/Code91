def create_file_directory_matrix(depth, width):
    matrix = [[''] * width for _ in range(depth)]
    return matrix

def create_file(matrix, depth, width, name):
    if depth >= len(matrix) or width >= len(matrix[depth]):
        # Expand matrix size if necessary
        expand_matrix(matrix, depth, width)

    matrix[depth][width] = name

def expand_matrix(matrix, target_depth, target_width):
    current_depth = len(matrix)
    current_width = len(matrix[0])

    if target_depth >= current_depth:
        for _ in range(target_depth - current_depth + 1):
            matrix.append([''] * current_width)

    if target_width >= current_width:
        for row in matrix:
            row.extend([''] * (target_width - current_width + 1))
