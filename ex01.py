dp=[[0]*14 for i in range(15)]
for i in range(14):
    dp[0][i]=i+1
for i in range(1,15):
    for j in range(14):
        dp[i][j]=sum(dp[i-1][0:j+1])
for i in range(int(input())):
    print(dp[int(input())][int(input())-1])
