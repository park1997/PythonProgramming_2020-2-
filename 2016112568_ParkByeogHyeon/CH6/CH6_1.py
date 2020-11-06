f=open('D:/Python/Atom/2016112568_ParkByeogHyeon/CH6/CH6_Hey_Jude.txt','r')
s=f.readlines()
result=''
for i in s:
    result+=i
print("Jude word count is {}".format(result.count("Jude")))
print("NA/na word count is {}".format(result.count("Na")+result.count("na")))
print(result.replace("Jude","ByeongHyeon"))
f.close()
