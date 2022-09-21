#BeautifulSoup 기능

from bs4 import BeautifulSoup  #파싱, 파서를 위해서 모듈 사용
from os import * # 운영체제가 기본으로 제공하는 모듈 

#htmlcode = BeautifulSoup("<div><span>테스트</span></div>")
#soup = BeautifulSoup("<span><b><i>테스트</i></span>")
#print(htmlcode.prettify())
#print(soup.prettify())

directory = "html"
print(getcwd())  #getcwd : 현재 (파이선)경로
mkdir(directory) #mkdir  : (make dir) 디렉토리 생성



