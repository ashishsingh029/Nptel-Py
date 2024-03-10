a = int(input())
b = int(input())
c = int(input())
if c*c == a*a + b*b or a*a == b*b + c*c or b*b == a*a + c*c:
  print("YES",end='')
else:
  print("NO",end='')