f_name8=open('name2008.txt','r')
f_name15=open('name2015.txt','r')
s_name8=f_name8.readlines()
s_name15=f_name15.readlines()
result_dic_f_8={}
result_dic_m_8={}
for i in s_name8:
    x=i.replace("\n","").split(",")
    if x[1]=="F":
        if x[0] not in result_dic_f_8:
            result_dic_f_8[x[0]]=int(x[2])
        else:
            result_dic_f_8[x[0]]+=int(x[2])
    elif x[1]=="M":
        if x[0] not in result_dic_m_8:
            result_dic_m_8[x[0]]=int(x[2])
        else:
            result_dic_m_8[x[0]]+=int(x[2])

result_dic_f_15={}
result_dic_m_15={}
for i in s_name15:
    x=i.replace("\n","").split(",")
    if x[1]=="F":
        if x[0] not in result_dic_f_15:
            result_dic_f_15[x[0]]=int(x[2])
        else:
            result_dic_f_15[x[0]]+=int(x[2])
    elif x[1]=="M":
        if x[0] not in result_dic_m_15:
            result_dic_m_15[x[0]]=int(x[2])
        else:
            result_dic_m_15[x[0]]+=int(x[2])

for i in result_dic_f_15:
    if i in result_dic_f_8 and i in result_dic_f_15:
        result_dic_f_15[i]-=result_dic_f_8[i]
    if i in result_dic_m_8 and i in result_dic_m_15:
        result_dic_m_15[i]-=result_dic_m_8[i]
name_dic_f=sorted(result_dic_f_15.items(), key=lambda x: int(x[1]), reverse=True)
name_dic_m=sorted(result_dic_m_15.items(), key=lambda x: int(x[1]), reverse=True)
for i in range(10):
    print(name_dic_f[i][0],name_dic_f[i][1])
print()
for i in range(10):
    print(name_dic_m[i][0],name_dic_m[i][1])
