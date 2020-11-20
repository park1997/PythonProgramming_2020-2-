import pandas as pd
df_timeline=pd.read_excel("timeline.xlsx")
print(df_timeline)

df_timeline=df_timeline.append({"작성자":"이름1","작성시간":"시간","글내용":"글내용","좋아요수":"좋아요수","평점":"평점","과목명":"과목명","글제목":"글제목"},ignore_index=True)
df_timeline.to_excel("timeline.xlsx",index=False)
print(df_timeline)

#df_timeline.drop(df_timeline.loc[df_timeline["작성자"]=="이름1"].index,inplace=True)


#df_timeline.to_excel("timeline.xlsx",index=False)
#print(df_timeline)
#for i,j in enumerate(df_timeline["글제목"]):
#    print(i,j)
#print(enumerate(df_timeline["글제목"]))
pd.options.mode.chained_assignment = None
df_timeline["작성자"][0]="박병현"
df_timeline.to_excel("timeline.xlsx",index=False)
print(df_timeline)
print(df_timeline["작성자"][1])
