import pandas as pd
import numpy as np
class test:
    df_timeline=pd.read_excel("timeline.xlsx")
    df_idpw=pd.read_excel("ID,PW.xlsx")

    def __init__(self,name):
        self.name=name

df_timeline=pd.read_excel("timeline.xlsx")

head_name=[i for i in df_timeline["과목명"]]
head_name=list(set(head_name))

a=df_timeline[["과목명","평점"]]
#print(a)
print(head_name)
b=[]
for i in head_name:
    b.append([i,round(a["평점"].loc[a["과목명"]==i].mean(),4)])
b=sorted(b, key=lambda x:x[1],reverse=True)
for i,j in enumerate(b):
    print("{} - {} :\t{}점".format(i+1,j[0],j[1]))
