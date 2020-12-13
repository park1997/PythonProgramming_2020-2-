from collections import deque
import sys
a=int(sys.stdin.readline())
result=deque()
real=deque()
for i in range(a):
    b=int(sys.stdin.readline())
    x=0
    y=len(result)-1
    while x<=y:
        mid=(x+y)//2
        if result[mid]<b:
            x=mid+1
        else:
            y=mid-1
    if x>=len(result):
        result.append(b)
    else:
        result.insert(x,b)

    if len(result)%2==0:
        real.append(result[((len(result)+1)//2)-1])
    else:
        real.append(result[((len(result)+1)//2)-1])
for i in real:
    print(i)
