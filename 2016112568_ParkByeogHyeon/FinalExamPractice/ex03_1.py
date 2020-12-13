f_name0=open('name2000.txt','r')
f_name1=open('name2001.txt','r')
f_name2=open('name2002.txt','r')
f_name3=open('name2003.txt','r')
f_name4=open('name2004.txt','r')
f_name5=open('name2005.txt','r')

print("{}\t{}\t{}\t{}\t{}".format("YEAR","FEMALE","MALE","TOTAL","RATE %"))
print("{}".format("="*50))
s_0=f_name0.readlines()
s_1=f_name1.readlines()
s_2=f_name2.readlines()
s_3=f_name3.readlines()
s_4=f_name4.readlines()
s_5=f_name5.readlines()
male_0=0
female_0=0
for i in s_0:
    info=i.replace("\n","").split(",")
    if info[1]=="M":
        male_0+=int(info[2])
    else:
        female_0+=int(info[2])

male_1=0
female_1=0
for i in s_1:
    info=i.replace("\n","").split(",")
    if info[1]=="M":
        male_1+=int(info[2])
    else:
        female_1+=int(info[2])
male_2=0
female_2=0
for i in s_2:
    info=i.replace("\n","").split(",")
    if info[1]=="M":
        male_2+=int(info[2])
    else:
        female_2+=int(info[2])
male_3=0
female_3=0
for i in s_3:
    info=i.replace("\n","").split(",")
    if info[1]=="M":
        male_3+=int(info[2])
    else:
        female_3+=int(info[2])
male_4=0
female_4=0
for i in s_4:
    info=i.replace("\n","").split(",")
    if info[1]=="M":
        male_4+=int(info[2])
    else:
        female_4+=int(info[2])
male_5=0
female_5=0
for i in s_5:
    info=i.replace("\n","").split(",")
    if info[1]=="M":
        male_5+=int(info[2])
    else:
        female_5+=int(info[2])
print("{}\t{}\t{}\t{}\t{}%".format(2000,male_0,female_0,male_0+female_0,"100.0"))
print("{}\t{}\t{}\t{}\t{:.6}%".format(2001,male_1,female_1,male_1+female_1,(male_1+female_1)*100/(male_0+female_0)))
print("{}\t{}\t{}\t{}\t{:.6}%".format(2002,male_2,female_2,male_2+female_2,(male_2+female_2)*100/(male_1+female_1)))
print("{}\t{}\t{}\t{}\t{:.6}%".format(2003,male_3,female_3,male_3+female_3,(male_3+female_3)*100/(male_2+female_2)))
print("{}\t{}\t{}\t{}\t{:.6}%".format(2004,male_4,female_4,male_4+female_4,(male_4+female_4)*100/(male_3+female_3)))
print("{}\t{}\t{}\t{}\t{:.6}%".format(2005,male_5,female_5,male_5+female_5,(male_5+female_5)*100/(male_4+female_4)))
