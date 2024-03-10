string = input()
ans = 0
for char in string:
    ans = ans*26 + (ord(char) - ord('A') + 1)
print(ans,end='')