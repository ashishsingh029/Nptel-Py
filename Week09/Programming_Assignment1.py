def balanced(word):
    stack = []
    for ch in word:
        if ch == '(':
            stack.append(')')
        elif ch == '{':
            stack.append('}')
        elif ch == '[':
            stack.append(']')
        elif len(stack) == 0 or ch != stack[-1]:
            return False
        else:
            stack.pop()
            
    return len(stack) == 0
