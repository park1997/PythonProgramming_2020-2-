f_name15=open('name2015.txt','r')
s_name15=f_name15.readlines()
result_dic_m={}
result_dic_f={}
for i in s_name15:
    x=i.replace("\n","").split(",")
    if x[1]=="M":
        if x[0] not in result_dic_m:
            result_dic_m[x[0]]=x[2]
        else:
            result_dic_m[x[0]]+=x[2]
    elif x[1]=="F":
        if x[0] not in result_dic_f:
            result_dic_f[x[0]]=x[2]
        else:
            result_dic_f[x[0]]+=x[2]

name_dic_f=sorted(result_dic_f.items(), key=lambda x: int(x[1]), reverse=True)
name_dic_m=sorted(result_dic_m.items(), key=lambda x: int(x[1]), reverse=True)

for i in range(10):
    print("{:5}\t{:10}\t{:10}".format(i+1,name_dic_f[i][0],name_dic_f[i][1]))
print()

for i in range(10):
    print("{:5}\t{:10}\t{:10}".format(i+1,name_dic_m[i][0],name_dic_m[i][1]))
