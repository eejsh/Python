from bs4 import BeautifulSoup
from requests import *
from re import * #정규식코드 - 문자열치환
from random import *

#크롤링 사용되는 파라미터 page view 
pno_data = ["69382","70931","69389","69388"] #파라미터값 추가 시 계속 가져옴..
test = range(1,22) # 페이지번호..

#해당 page view 배열을 순차적으로 접근 할 수 있도록 반복문 실행
for pno in pno_data:
#해당 파라미터 배열값을 입력시켜 배열이 끝날때까지 크롤링함
 #url = "https://pages.coupang.com/p/"+ pno +"?from=home_C2&traid=home_C2&trcid=11186418"
 url = "https://pages.coupang.com/p/69382?from=home_C2&traid=home_C2&trcid=11186418"
 
 html = get(url)
 html.raise_for_status()

 code = BeautifulSoup(html.text, "lxml")
 product = code.find("ul", attrs={"id":"products"})
 lis = product.find_all("li")
 
              
 for no in lis:
   product_name = no.find("div", attrs={"class":"name"}) #상품명
   product_money = no.find("strong", attrs={"class":"price-value"}) #상품가격
   product_count = no.find("span", attrs={"class":"rating-total-count"}) #추천수
   product_img = no.find("img")
   pd_img = "http:" + product_img["lazy-load"]  
  
   # product_img["lazy-load"] - attrs 에서 해당 속성을 가져오지 못함. 정상적인 속성값이 아닌 임의값이여서 로드못함! (class, name 값이 아님.)
   # 임의 생성된 속성값은 [] 배열 형태로 로드 하면 쉽게 가져올 수 있음.
   
   
   #해당 상품 이미지를 모두 로드하였음.
   #code = randrange(1, 9000) #새로운 이미지명을 random으로 설정. 
   #imgload = get(pd_img) #해당 url로 이미지를 가져옴
   
   #with open("product{0}.jpg".format(code),"wb") as i :
   #     i.write(imgload.content) #해당 경로에 이미지를 모두 저장시킴
        
      
      
   if product_count:
    rate = product_count.get_text()
    rate_txt = sub(r"[(,)]", "", rate) # () 없애기. 정규식코드 [a-z].. [(,)]
   else :    
    rate_txt ="등록된 평점이 없습니다."

  # print(rate_txt)
       
 
 
 
 #replace: 1개의 단어만 수정할시..    
 #("," , "", 1) 1개만 수정
 #(",", "") 해당되는 모든 단어를 수정
  
 #sub(정규식코드, 파이선) re 라는 모듈을 import 해야 사용가능.  : 여러개의 단어 수정시 
  
   money = product_money.get_text() #금액만 출력하기 get_text()
   money_txt = money.replace(",", "")
   #print(money_txt)
  
   product_name_txt = product_name.get_text()
   pdtxt = product_name_txt.strip() #strip 줄바꿈 및 공백
   pdtxt2 = pdtxt.replace(", ", " ") #쿠팡 상품명에 , 로 구분자를 없앰
   #print(pdtxt2)
  
  
  
  
  