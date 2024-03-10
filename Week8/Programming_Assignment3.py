def two_level_sort(scores):
    n = len(scores)
    for i in range(n-1):
        for j in range(n-i-1):
            if scores[j][1] > scores[j+1][1]:
                scores[j], scores[j+1] = scores[j+1], scores[j]
            elif scores[j][1] == scores[j+1][1]:
                if scores[j][0] > scores[j+1][0]:
                    scores[j], scores[j+1] = scores[j+1], scores[j]

    return scores