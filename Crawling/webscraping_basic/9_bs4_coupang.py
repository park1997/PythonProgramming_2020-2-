import requests
from bs4 import BeautifulSoup
import re

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
# 서버가 나를 막음 그래서 headers를 이용하여 진짜 사용자가 이용하는 것처럼 만듬
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
res= requests.get(url,headers=headers)
res.raise_for_status()
soup=BeautifulSoup(res.text,"lxml")
items= soup.find_all("li",attrs={"class":re.compile("^search-product")})

# print(items[0].find("div",attrs={"class":"name"}).get_text())
for item in items:
    name=item.find("div",attrs={"class":"name"}).get_text() # 제품명
    price= item.find("strong",attrs={"class":"price-value"}).get_text() # 가격
    rate=item.find("em",attrs={"class":"rating"}).get_text() # 평점
    rate_count = item.find("span",attrs={"class":"rating-total-count"}).get_text()[1:-1] # 리뷰 수
    print(name,price,rate,rate_count)
        




