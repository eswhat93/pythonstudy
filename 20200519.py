# 파이썬 웹 크롤링
# 크롤링 = 웹상 존재하는 컨텐츠 수집 / 프로그래밍으로 자동화 가능
# BeautifulSoup 라이브러리 활용한 예제
# 파이썬 설치 위치에서 scripts폴더로 이동하여 pip 명령어로 설치
# cmd > cd C:\Users\admin\AppData\Local\Programs\Python\Python37-32\Scripts > pip install beautifulsoup4

#requests(HTTP 요청처리 위해 사용하는 모듈 / 기본 내장 모듈이 아니라 설치해줘야함) 모듈도 설치해준다
import requests
from bs4 import BeautifulSoup

#rees 객체에 HTML 데이터가 저장되고, res.content로 데이터를 추출
res = requests.get('https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=105&oid=015&aid=0004343519')
#print(res.content)

soup = BeautifulSoup(res.content,'html.parser')

title = soup.find('title')

print(title.get_text())


