import pandas as pd
import numpy as np
class test:
    df_timeline=pd.read_excel("timeline.xlsx")
    df_idpw=pd.read_excel("ID,PW.xlsx")

    def __init__(self,name):
        self.name=name


df_idpw=pd.read_excel("ID,PW.xlsx")
df_timeline=pd.read_excel("timeline.xlsx")

print(df_idpw["아이디"])
#pd.options.mode.chained_assignment = None
#df_idpw.loc[df_idpw.아이디=="asd","아이디"]="시1발"
#for a,b,c,d in enumerate(df_idpw):
#    print(a,b,c,d)
pd.options.mode.chained_assignment = None
df_timeline["좋아요수"].iloc[0]="hello my name is byunghyun"
if "byunghyun" in df_timeline["좋아요수"].iloc[0].split():
    print(1)
else:
    print(2)
print(df_timeline["좋아요수"].iloc[3])
