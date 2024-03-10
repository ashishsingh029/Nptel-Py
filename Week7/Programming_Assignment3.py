ip = input()
ans = ""
for char in ip:
  ans += chr(ord('z') + ord('a') - ord(char))
print(ans,end='')