def distance(word_1, word_2):   
    ans = 0
    if len(word_1) != len(word_2):
        return -1
    for i in range (len(word_1)):
        ans += abs(ord(word_1[i]) - ord(word_2[i]))
    return ans
word1 = input()
word2 = input()

result = distance(word1, word2)
print(result)