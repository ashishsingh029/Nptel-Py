n = int(input())
A = []
for i in range(n):
    row = list(map(int, input().split(" ")))
    A.append(row)
s = int(input())
for i in range(n):
    for j in range(n):
        A[i][j] *= s
for row in A:
    for j in range(n-1):
        print(row[j],e