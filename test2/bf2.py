from bs4 import *
from os import *
from requests import * # requests : 해당 url 접속 정보를 확인


url = get("https://www.naver.com/")
print("응답코드:", url.status_code) # 200 :정상

if url.status_code == codes.ok:
     print(url.text)
     print("웹사이트 정상적인 페이지 입니다.")
else :
     print("해당 웹사이트는 보안 또는 코드에 문제가 있습니다. ")     
 



'''
웹 스크래핑 : 데이터만 웹사이트 가저오는 부분

웹 크롤링 : 웹 페이지에 모든 정보를 저장 하는 부분

''' 