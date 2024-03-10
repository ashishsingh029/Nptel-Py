n = int(input())
A = []
B = []
for i in range(n):
    A.append(list(map(int, input().split(","))))
for i in range(n):
    B.append(list(map(int, input().split(","))))
AxB = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            AxB[i][j] += A[i][k] * B[k][j]
for row in AxB:
    for j in range(n-1):
        print(row[j],end=',')
    print(row[n-1])