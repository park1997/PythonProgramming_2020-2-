a=list(map(str,input().split()))
for i in range(len(a)):
    num,string=map(str,a[i].split("."))
    a[i]="{}.{}".format(num.rjust(3,"0"),string)
print(a)
