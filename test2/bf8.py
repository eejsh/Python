from bs4 import BeautifulSoup
from requests import *
from re import * #정규식코드 - 문자열치환
from random import *
from csv import *  #csv파일로 변환 할 수 있는 모듈

filenm = "kospi.csv"
f = open(filenm,"w",encoding="euc-kr", newline="") 
#csv파일 저장 시 euc-kr 적용 시 한글 깨짐현상 없어짐..

#newline : csv에 데이터 등록 시 한칸 띄어쓰기가 되는 경우 있음.
# 해당 속성을 입력 시 띄어쓰기 기능 없앰 (newline="")
#filenm, "w" -> "a" 로 바꾸면 누적해서 저장가능!

writer = writer(f)

#크롤링
url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=1"

web = get(url)
web.raise_for_status()
html = BeautifulSoup(web.text,"lxml")
table = html.find("table", attrs={"class": "type_2"})  #<table summary="코스피 시세정보를 선택한 항목에 따라 정보를 제공합니다." cellpadding="0" cellspacing="0" class="type_2">
tbody = table.find("tbody")
tr = tbody.find_all("tr")

 
for data in tr :
      td = data.find_all("td")
      data = [text.get_text() for text in td]
      if len(data) <=1 : 
         continue
      else :
         company = data[1]
         price = data[2].strip().replace(",","")
         face = data[3].strip().replace(",","")
         print(company, price, face)  #배열화 시켜야함
         
         #writer.writerow(company)   #writerow : 엑셀 기준에 , 입력시켜서 다음칸으로 적용되는 형태
         
         rowdata = [company,price,face]  # 배열로 생성 해야만 csv에서 하나 행, 열로 인식됨. 
         writer.writerow(rowdata)



#<tr onmouseover="mouseOver(this)" onmouseout="mouseOut(this)" style="background-color: rgb(255, 255, 255);">
 