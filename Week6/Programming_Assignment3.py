def steps(n):
    if n <= 2:
      return n
    if n == 3:
      return 4
    return steps(n-1) + steps(n-2) + steps(n-3)
n = int(input())
print(steps(n))