def ancestry(P, present, past):
    ans = []
    while present != past:
        ans.append(present)
        present = P[present]
    ans.append(past)
    return ans
P = input()
P = eval(P)
present = input()
past = input()

result = ancestry(P, present, past)
print(result)