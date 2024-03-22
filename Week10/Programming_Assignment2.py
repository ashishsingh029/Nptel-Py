def is_magic(matrix):
    n = len(matrix)
    magic_sum = sum(matrix[0])
    for i in range(n):
        if sum(matrix[i]) != magic_sum:
            return "NO"
        if sum(matrix[j][i] for j in range(n)) != magic_sum:
            return "NO"
    if sum(matrix[i][i] for i in range(n)) != magic_sum:
        return "NO"
    if sum(matrix[i][n-i-1] for i in range(n)) != magic_sum:
        return "NO"

    return "YES"
