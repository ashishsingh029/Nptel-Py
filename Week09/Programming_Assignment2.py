def depth(exp):
    count = 0
    ans = 0
    for ch in exp:
        if ch in [ '(', '{', '[' ]:
            count = count + 1
        else:
            ans = max(ans, count)
            count = count - 1
    return ans
