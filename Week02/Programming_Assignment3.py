def isValidPass(pwd):
    if len(pwd) < 8 or len(pwd) > 32:
        return False
    if not pwd[0].isalpha():
        return False;
    for c in pwd:
        if c == '\\' or c == '/' or c == '=' or c == "'" or c == '"' or c == ' ':
            return False
    return True
    
pwd = input()
isValid = isValidPass(pwd)
print(isValid, end= '')