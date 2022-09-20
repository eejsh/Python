#BeautifulSoup(bs4) 사용하기 위해서는 라이브러리를 pom.xml 처럼 파이선에 등록시켜 주셔야 합니다.
#cmd에서 등록

'''
설치형태: cmd로 설치

1. 파이선 설치된 디렉토리 경로를 확인 cd
C:\Users\tjoeun\AppData\Local\Programs\Python\Python310\
2. cd 이용하여 해당 디렉토리 이동 
cd Scripts
3. script 디렉토리 이동  
dir/w
4. pip install beautifulsoup4 ...

단, 파이선 삭제 후 재설치 시 재설치요함.
'''


#url open 함수: 원하는 웹페이지 주소 접속 및 연결 

from urllib.request import urlopen

from bs4 import BeautifulSoup
# BeautifulSoup 함수 : 접속한 웹페이지에 대한 모든 문서파일 파서하는 역활을 하게 됩니다.

#urlopen(웹페이지 주소)
html = urlopen("https://entertain.naver.com/read?oid=421&aid=0006345203")  

#해당 url parser작업을 함
object = BeautifulSoup(html, "html.parser")

#해당 parser 문자를 html 로 저장함 
files = open("news.html", "w", encoding="utf-8")
print(object, file=files)
files.close()


#인터넷 신문사에서 크롤링 많이 사용함.
