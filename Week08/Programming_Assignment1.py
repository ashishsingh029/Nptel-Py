ans = []
for i in range(8):
    ip = input().split(",")
    ans.append([ip[0], len(ip) - 1])

n = len(ans)
for i in range(n-1):
    for j in range(n-i-1):
        if ans[j][1] < ans[j+1][1]:
                ans[j], ans[j+1] = ans[j+1], ans[j]
        elif ans[j][1] == ans[j+1][1]:
            if ans[j][0] > ans[j+1][0]:
                ans[j], ans[j+1] = ans[j+1], ans[j]
                
for team, points in ans:
    print(f"{team}:{points}")
  	