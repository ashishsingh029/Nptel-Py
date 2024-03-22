def rotate(mat):
    rows = len(mat)
    cols = len(mat[0])
    matTAndRev = [[mat[i][j] for i in range(rows-1, -1, -1)] for j in range(cols)]
    return matTAndRev
