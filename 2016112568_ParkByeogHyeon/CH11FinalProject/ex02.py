import pandas as pd
class test:
    df_timeline=pd.read_excel("timeline.xlsx")
    df_idpw=pd.read_excel("ID,PW.xlsx")

    def __init__(self,name):
        self.name=name


df_idpw=pd.read_excel("ID,PW.xlsx")
print(df_idpw)
pd.options.mode.chained_assignment = None
df_idpw.loc[df_idpw.아이디=="asd","아이디"]="시1발"
for a,b,c,d in enumerate(df_idpw):
    print(a,b,c,d)
