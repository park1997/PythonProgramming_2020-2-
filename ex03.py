import csv
f = open("usa_alcohol_comsumption_data.csv", 'r')
reader = csv.reader(f)
a={}
a_num={}
nothing=0
for i in reader:
    nothing+=1
    if nothing==1:
        continue
    if 2000<=float(i[1]) and float(i[1])<=2009:
        if i[0] not in a:
            a[i[0]]=[float(i[2]),float(i[3]),float(i[4])]
        else:
            a[i[0]][0]+=float(i[2])
            a[i[0]][1]+=float(i[3])
            a[i[0]][2]+=float(i[4])
        if i[0] not in a_num:
            a_num[i[0]]=1
        else:
            a_num[i[0]]+=1

print(a)
print()
for i in a:
    a[i][0]=a[i][0]/a_num[i]
    a[i][1]=a[i][1]/a_num[i]
    a[i][2]=a[i][2]/a_num[i]
print(a)

a=sorted(a.items(), key= lambda x:x[1][1], reverse=True)
print()
print(a)
