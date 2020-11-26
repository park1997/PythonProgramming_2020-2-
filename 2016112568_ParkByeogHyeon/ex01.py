from bs4 import BeautifulSoup
import lxml
import requests
sw_url="https://itcec.dongguk.edu/bbs/board.php?bo_table=itedu4_11&page=2&page=1"
sw_res= requests.get(sw_url)
#혹시나 프로그램에 문제가 생기면 종료를 하도록 함.
sw_res.raise_for_status()
#sw_soup은 모든 정보를 가지고 있다.
sw_soup=BeautifulSoup(sw_res.text,"lxml")
sw_info=sw_soup.title.get_text()
print(sw_info)
print()
sw_info1=sw_soup.table.td.find_all("a",attrs={"style":"font-weight:bold;color:#000000;"})

#print(sw_info)
#공지사항(공지)
ballground=[]
for i in sw_info1:
    ballground.append(i.get_text())

a_tag=sw_soup.select("a")
result=[]
for i in a_tag:
    result.append(i.get_text())
del result[:result.index(ballground[0])]
del result[:result.index(ballground[-1])]
result=[i for i in result if len(i)>5]
print()
print(ballground)
print(result)
