import re
import lxml
import requests
from bs4 import BeautifulSoup
import csv

filename="시가총액1-200.csv"
# 엑셀파일에서 열떄 한글이 깨진다그러면은 utf-8-sig 을 사용하자 !
f=open(filename,"w",encoding="UTF-8-sig",newline="")
# writer 를 이용하여 파일을 쓸 수있음
writer = csv.writer(f)

headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
url="https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=1"
res=requests.get(url,headers=headers)
res.raise_for_status()
soup=BeautifulSoup(res.text,"lxml")
data_rows=soup.find("table",attrs={"class":"type_2"}).find("tbody").find_all("tr")
for row in data_rows:
    colums= row.find_all("td")
    # 의미없는 데이터는 skip
    if len(colums)<=1:
        continue
    data=[column.get_text().strip() for column in colums]
    writer.writerow(data)
    


