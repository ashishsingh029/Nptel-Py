def minor_matrix(M, i, j):
    for row in M:
        row.pop(j)
    M.pop(i)
    return M
