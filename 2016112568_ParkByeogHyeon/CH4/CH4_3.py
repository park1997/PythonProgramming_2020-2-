#LIS
a_1,a_2,a_3=map(int,input().split())
a=[a_1,a_2,a_3]
real=[]
for i in a:
    x=0
    y=len(real)-1
    while x<=y:
        mid=(x+y)//2
        if real[mid]<i:
            x=mid+1
        else:
            y=mid-1
    if x>=len(real):
        real.append(i)
    else:
        real.insert(x,i)
print(real[1])

#sort

#a_1,a_2,a_3=map(int,input().split())
#a=[a_1,a_2,a_3]
#a.sort()
#print(a[1])
