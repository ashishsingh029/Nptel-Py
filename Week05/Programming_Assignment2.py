real_dict = {}
i_str = list(input().split(","))
for s in i_str:
    ch = s[0]
    if ch not in real_dict:
        real_dict[ch] = []
        real_dict[ch].append(s)
    else:
        real_dict[ch].append(s)

for key, value in real_dict.items():
    print(f'{key}:{",".join(value)}')