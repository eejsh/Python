from tkinter import *
from _functools import partial


#gui

root = Tk()
root.title("크롤링")
root.geometry("640x150")  #가로 X 세로

msg = Label(root, text="크롤링 주소 형식 ")
msg2 = Label(root, text="예시) http://search.aa.co.kr/search/?keyword=검색어")

msg.pack()
msg2.pack()


###입력파트###

src = Text(root,width=50, height=3) # 크롤링 주소입력
src.insert(END, "") # 사용자가 입력한 주소값을 전달받기 위한 코드
src.place(x=50, y=50) #원하는 위치에 오브젝트를 설정할 수 있습니다. 
#src.pack(side="left")


#def crawlings():
#     showinfo("알림","크롤링준비중") # msgbox=alret과 같음

#일반적인 import 방식
#import crawling_def as craw
# btn = Button(root, width=10, height=3, text="크롤링 시작", command= craw.crawlings) import로 불러 올 시 craw.crawlings 
                                                                 #crawlings("홍길동") 인자값 태워보내기 , crawlings(data) 선언해야 받아 처리가능

#from형태의 import방식
#partial (함수명, "인자값")
from crawling_def import * # crawlings # from으로 가져올 시 crawlings만불러와두됨. 


#partial, lambda 값 보내는 방식 2가지.
#btn = Button(root, width=10, height=3, text="크롤링 시작", command= partial(crawlings,"홍길동"))
#btn = Button(root, width=10, height=3, text="크롤링 시작", command= lambda:crawlings())           


def textload():
     ### 사용자가 입력한 값을 변수로 변환 ###
     url = src.get("1.0", END)
#crawling_def.py 함수로 값을 전달
     crawlings(url)

btn = Button(root, width=10, height=3, text="크롤링 시작", command= textload)
#버튼에서 값을 바로 보낼수 없음. 변수를 받아서 crawling_def로 거쳐 보내야됨. 


btn.place(x=450, y=50)
#btn.pack(side="right")



root.resizable(False, False)
root.mainloop() #실행 . 무조건 맨 아래에 생성 

#C:\python1>cd test2 crawling.py 있는 경로로 가서 pyinstaller -w crawling.py 선언 하면 .exe 파일 만들어짐.
# https://browse.auction.co.kr/search?keyword=%ED%8E%9C%EC%85%98%EC%98%88%EC%95%BD