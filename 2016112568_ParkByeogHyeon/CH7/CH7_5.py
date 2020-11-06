key=list(map(str,input().split()))
item=list(map(int,input().split()))
result={}
for i in range(len(key)):
    if item[i]!=30:
        result[key[i]]=item[i]
del result["delta"]
print(result)
