def matrix_multiply(A, B):
    n = len(A)
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    return result
  
def power(A, m):
    Axm = A
    for i in range(1, m):
        Axm = matrix_multiply(Axm, A)
    return Axm
