import requests
from bs4 import BeautifulSoup

url = "https://corners.gmarket.co.kr/superdeals"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

# 첫 번째 li 요소의 a 태그 href 속성 값 추출
fullxpath_url = soup.select_one("li:nth-child(1) > div > a")["href"]

print(fullxpath_url)
