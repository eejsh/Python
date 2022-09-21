from bs4 import BeautifulSoup
from os import *
from requests import *
from tkinter import *

from idlelib.iomenu import encoding
from test.test_urllib import urlopen



root = Tk()
root.title("웹페이지 크롤링")
root.geometry("500x100")
root.resizable(False, False)

url = Text(root, width =40, height=2)
url.pack()
url.insert(END, "URL를입력하세요.")


def pageload():
     urladdr = url.get(0.1,END)
     check = get(urladdr)
     #해당 접속 페이지 확인 후 정상적인 웹 크롤링 test.html로 파일 저장
     if check.status_code == codes.ok:
          html = urlopen(urladdr)
          object = BeautifulSoup(html, "html.parser")
          files = open("test.html", "w", encoding="utf-8")
          
          print(object,file=files)
          files.close()

          print("생성완료 되었습니다. 모든 크롤링 완료")
          
     else:
          print("올바른 웹페이지가 아닙니다.")
             
btn = Button(root, text="웹크롤링", command = pageload)
btn.pack()
root.mainloop()          