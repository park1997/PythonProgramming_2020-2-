f_name0=open('name2000.txt','r')
f_name1=open('name2001.txt','r')
f_name2=open('name2002.txt','r')
f_name3=open('name2003.txt','r')
f_name4=open('name2004.txt','r')
f_name5=open('name2005.txt','r')
s_name0=f_name0.readlines()+f_name1.readlines()+f_name2.readlines()+f_name3.readlines()+f_name4.readlines()+f_name5.readlines()
# 이름 성 번호
name_dic_m={}
name_dic_f={}
for i in s_name0:
    i=i.replace("\n","")
    a=list(i.split(","))
    if a[1]=="F":
        if a[0] not in name_dic_f:
            name_dic_f[a[0]]=0
            name_dic_f[a[0]]+=int(a[2])
        else:
            name_dic_f[a[0]]+=int(a[2])
    else:
        if a[0] not in name_dic_m:
            name_dic_m[a[0]]=0
            name_dic_m[a[0]]+=int(a[2])
        else:
            name_dic_m[a[0]]+=int(a[2])

name_dic_m=sorted(name_dic_m.items(), key=lambda x:x[1], reverse=True)
name_dic_f=sorted(name_dic_f.items(), key=lambda x:x[1], reverse=True)
# print(name_dic_m)
print()
print()
# print(name_dic_f)
man=[]
female=[]
for i in range(10):
    man.append(name_dic_m[i])
for i in range(10):
    female.append(name_dic_f[i])


print("{}".format("-"*30))
print("2000~2018 가장 인기있는 아이 이름 TOP10")
print("{}".format("-"*30))
for i in range(10):
    print("{}\t\t{}\t\t{}\t\t{}\t\t{}".format(i+1,female[i][0],female[i][1],man[i][0],man[i][1]))
