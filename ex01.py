import sys
a=sys.stdin.readline()
b=sys.stdin.readline()
dp=[[0]*(len(b)+1)  for i in range(len(a))]
for i in range(1,len(a)):
    for k in range(1,len(b)+1):
        if a[i-1]==b[k-1]:
            dp[i][k]=dp[i-1][k-1]+1
        else: dp[i][k]=max(dp[i-1][k],dp[i][k-1])
print(dp[-1][-1])
