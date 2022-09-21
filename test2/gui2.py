from tkinter import *
from pkg_resources._vendor.jaraco.context import null

root = Tk()
root.title("연습프로그램")
root.geometry("500x500")
root.resizable(False, False)

txt = Entry(root, width=30) #Entry 한줄자리 input (height 설정안됨..고정높이)
#Text로 사용할 경우 insert와함께 적용해야함.  (width, height 사용됨)
txt.pack()

txt2 = Text(root, width=30, height=2)
txt2.pack()
txt2.insert(END, "memo")

def aaa() :
    url = txt.get() 
    url2 = txt2.get(0.1, END) #Text (1.0)   (1="첫번째 행 ". 0="열의 첫번째 위치" , end=(마지막단어까지)
    print(url2)
    print(url)
 
btn = Button(root, width=8, height=2, text="크롤링", command =aaa)
btn.pack()

root.mainloop()



