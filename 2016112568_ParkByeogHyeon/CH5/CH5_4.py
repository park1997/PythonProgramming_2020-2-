#12자리 이상의 숫자는 필요가 없다
a = int(input())
dp = [0]*1000001
dp[1] = 1
for i in range(2,a+1):
    dp[i] = int(str(i * dp[i-1]).strip('0')[-12:])
print(str(dp[a]).rstrip('0')[-5:])



#재귀를 이용한 풀이
#import sys
#sys.setrecursionlimit(10**8)
#def f(x):
#    if x==0:
#        return 1
#    else:
#        return x*f(x-1)
#a=int(input())
#num=str(f(a))[::-1]
#result_number=0
#for i in range(len(num)):
#    if num[i]=='0':
#        pass
#    else:
#        result_number=i
#        break
#print(num[result_number:result_number+5][::-1])
#
