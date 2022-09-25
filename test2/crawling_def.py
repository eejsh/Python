from tkinter.messagebox import *
from tkinter import *
import requests      #통신 api json 형태로 변화 - 웹사이트에 접속하는 형태
from bs4 import BeautifulSoup
from re import *
from sqlite3 import *  #db연결
from dbconnect import *  #db 접속정보
from datetime import *

# messagebox=alert과 동일한 메세지 출력입니다.

  #showinfo : alert
  #showinfo("알림"," 크롤링준비중")
 

def crawlings(data):
     #if data.strip()=="":
     
     #주소가 10자 이하 일때.. 
     
     if len(data)==1 or 10 > len(data) :   # 빈공간에 데이터 있어서 if 걸러주기
          showinfo("경고", "크롤링할 url 주소를 입력하셔야 합니다.")
     else :  #크롤링파트
         # 문자열로 변환해야만 requests를 사용 할 수 있음.
        # try, except, finally 예외처리.
        print(data)
        try :
             
           
             
          # url = "http://www.naver.com"
          # url = "{}".format(data) # 문자열로 변환해야만 requests 를 사용할 수 있음. 

           url = data  #url에 공백이나 한글, 특수문자가 들어가 있을 경우 인식을 못해서 "{}".format(data) 선언해서 사용
           check = requests.get(url.strip(), headers={'User-Agent' :'Mozilla/5.1'})  # \n \ 빈 공간 제거. 
           ck = check.raise_for_status()      # NoneType(통신 Type)
         
           if str(ck) == "None":   
             html = BeautifulSoup(check.text, "lxml")
              
             #펜션이름
             div = html.find("div", attrs={"module-design-id" :"17"})
             div2 = div.find_all("div", attrs={"class" :"component--item_card"})
                    
             #titles = div2[1].find("span", attrs={"class" : "text--title"})
              
             #금액
             #money = div2[0].find("strong", attrs={"class": "text--price_seller"})
             #print(money)
              
             
             #db 접속정보 로드 
             con = connect.cursor()
             
               
             for z in div2 :
                titles = z.find("span", attrs={"class" : "text--title"})   #스크래핑 한것을 그대로
                money = z.find("strong",attrs={"class" : "text--price_seller"})
                money=sub(",","",money.text)  #money는 가공한번했음.. money로 출력
                print(titles.text)
                print(money)
                

                
                  #등록시간 
                #DB에서 날짜 입력을 저장 시키기 위해서 strftime : 문자열 형태의 시간으로 변경  
                
                now_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                
                  #DB저장
                sql = "insert into pension values('0','"+titles.text+"','"+money+"','"+now_date+"')"
                con.execute(sql)
                connect.commit()
              
           showinfo("성공", "정상적으로 모든 데이터를 스크래핑 완료 하였습니다. ")
        
        except :
           showinfo("실패", "크롤링 url 주소를 다시 확인하세요. ")
              
              
            
#pip install urllib3
     
        
        
        '''
        delete from pension 하고 
alter table pension auto_increment=1;   1번부터 데이터 들어감. 

create table pension(
     pidx int(4) not null auto_increment,
     pnm varchar(200) not null,
     pmoney char(7) not null,
     indate datetime not null default '0001-00-00 01:00:00',
primary key(pidx));
        '''