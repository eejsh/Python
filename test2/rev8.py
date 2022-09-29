#크롤링(html 로딩) & 스크래핑 (데이터끌어오기)

from bs4 import BeautifulSoup
from requests import *

url = "http://eejsh08.cafe24.com/site.html"

call = get(url)
call.raise_for_status()

htmlcode = BeautifulSoup(call.content.decode('utf-8', 'replace'), "lxml")

#class는 중복으로 사용할수 있음 id, name값으로 .
#li > ul  ul에서 li가 반복됨 , ul로 데이터를 긁어오면 li데이터 모두 긁기 가능
#id가 없을수 있음.. 

code = htmlcode.find("div", attrs={"class": "divcss"})
code2 = code.find("ul", attrs={"class" : "ulcss"})
code3 = code2.find_all("li") #<li>내용</li> 출력.
#li가 반복될 시 find_all (li 태그만 있고 class가 없을 시 attrs 필요없음)

array =[]

for txt in code3  :  
     array +=[txt.get_text()] #스크래핑 완료! array로 넣어주기


print(array)
     
     


     
     
     