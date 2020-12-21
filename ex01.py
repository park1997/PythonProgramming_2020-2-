#6
import sys
a=list(map(int,sys.stdin.readline().split()))
b=list(map(int,sys.stdin.readline().split()))
b.sort()
print(b[a[1]-1])

#5
from math import gcd
import sys
a,b=map(int,sys.stdin.readline().split())
print(gcd(a,b))

 # 3
 a={0:0,1:1,2:1}
def f(n):
    if n in a:
        return a[n]
    else:
        a[n] = f(n-2) + f(n-1)
        return a[n]
print(f(int(input())))




import sys
def f(x):
    num=set(range(2,x+1))
    for i in range(2,x+1):
        if i in num:
            num-=set(range(2*i,x+1,i))
    return len(num)
print(f(int(sys.stdin.readline())))
