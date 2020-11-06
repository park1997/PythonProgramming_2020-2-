dp={0:0,1:1,2:1}
a=int(input())
def f(x):
    if x in dp:
        return dp[x]
    else:
        dp[x]=f(x-2)+f(x-1)
        return dp[x]
print(f(a))
