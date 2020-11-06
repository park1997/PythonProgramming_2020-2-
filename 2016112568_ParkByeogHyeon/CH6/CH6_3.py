f=open('D:/Python/Atom/2016112568_ParkByeogHyeon/CH6/CH6_Hey_Jude.txt','r')
s=f.readlines()
result=""
for i in s:
    result+=i
print(len(result.replace("-"," ").replace(","," ").replace("("," ").replace(")", " ").split()))
f.close()
