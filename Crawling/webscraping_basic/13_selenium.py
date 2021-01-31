from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# chrome("여기에 경로를 넣어야함") 근데 우린 같은 폴더안에 있으니까 경로를 넣을 필요가 없음
browser = webdriver.Chrome("./chromedriver")
browser.get("http://naver.com")



