import requests
from bs4 import BeautifulSoup

url = "https://corners.gmarket.co.kr/superdeals"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

# fullxpath_url 추출
fullxpath_url = soup.select_one("li:nth-child(2) > div > a")["href"]

# fullxpath_url 링크로 접속해서 "대분류" 문자열 추출하기
response = requests.get(fullxpath_url)
soup = BeautifulSoup(response.text, "html.parser")
large_category = soup.select_one("html body div#root div.section__main div#content div.product-detail__top-wrap div.product-detail__title-area h2").text.strip()

# "대분류" 변수에 결과값 저장하기
대분류 = large_category

print(대분류)
