import pandas as pd

df=pd.read_csv("시가총액1-200.csv")
for i in range(len(df)):
    print("{} {} {}".format(df["종목명"][i],df["현재가"][i],df["전일비"][i]))

print(df["종목명"][0])