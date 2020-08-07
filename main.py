import requests
from bs4 import BeautifulSoup

URL = 'https://kr.indeed.com/jobs?q=python&l=seoul'

# 테스트 방법
page = requests.get(URL)
# print(page)

soup = BeautifulSoup(page.content, 'html.parser')

# print(soup.prettify())

# strip()
# 한 글의 제목 가져오는 거
# title = soup.find('h2', {'class':'title'}).text.strip()
# title2 = soup.find('a', {'id':'jl_d2df92c32bd4a203'})
# 전체 찾을 때 : find_all()

# print(title)

# 한 페이지 제목 다 가져오는 것
results = soup.find_all('div', {'class':'jobsearch-SerpJobCard'})
# print(results.prettify())

for result in results:
    title = result.find('h2', {'class':'title'}).text.strip()
    # company = 
    # location = 
    print(title, company, location)