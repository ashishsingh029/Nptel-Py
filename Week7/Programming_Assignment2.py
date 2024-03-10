ip = input()
queue = []
while ip != 'END':
    string = ip.split(",")
    if string[0] == 'JOIN':
        queue.append(int(string[1]))
    elif string[0] == 'PRINT':
        print(','.join(str(num) for num in queue))
    elif string[0] == 'LEAVE':
        queue.pop(0)
    elif string[0] == 'MOVE':
        token = int(string[1])
        if string[2] == 'HEAD':
          queue.remove(token)
          queue.insert(0, token)
        else:
          queue.remove(token)
          queue.append(token)
    ip = input()