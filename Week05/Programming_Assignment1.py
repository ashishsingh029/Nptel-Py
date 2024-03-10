def insert(L, x):

    uList = []
    i = 0
    while i < len(L) and L[i] < x:
        uList.append(L[i])
        i += 1
    uList.append(x)
    while i < len(L):
        uList.append(L[i])
        i += 1
    return uList
L = input().split(',')
L = [int(num) for num in L]

x = int(input())

result = insert(L, x)

# Printing the output
print(','.join(map(str, result)))