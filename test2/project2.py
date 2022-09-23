#pip install webdriver-manager

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriver, ChromeDriverManager

#자동 로그인, 자동페이지 이동, 자동검색 ...ㅋ
bw=webdriver.Chrome(ChromeDriverManager().install())
bw.get("https://www.naver.com/")          # 자동으로 크롬 브라우저 이동 

#파라미터 확인 하고 적용하면 수월함
# http://search.naver.com/search.naver?query= 
# http://search.daum.net/search?q = 
# https://www.google.com/search?q=


#search ="홍길동"
#bw.get("https://search.naver.com/search.naver?query="+search)
#search ="메롱"
#bw.get("https://search.naver.com/search.naver?query="+search)
#bw.get("https://search.daum.net/search?q="+search)
# search  배열로 넣으면 배열값 검색..
#search = ["a", "b" ,"c"]
#for aa in search:
#  bw.get("https://search.naver.com/search.naver?query="+search[aa])

#chromedriver

