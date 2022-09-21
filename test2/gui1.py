from tkinter import *


def abc():
     print("테스트인쇄")

def bbb():
     print("메롱")

root = Tk()
root.title("연습 프로그램") # 프로그램 타이틀 이름
root.geometry("500x500") # 가로크기 * 세로크기 
root.resizable(False, False) # 창 사이즈 자동조절 (기본 false, true시 조절가능)
btn1 = Button(root, text="메롱", command=abc)  # command 클릭 시 함수 호출 
btn2 = Button(root, width=10, height=2, text="메롱2", command=bbb)
#width=10 100px, height=2 20px
btn1.pack()
btn2.pack()
root.mainloop() #GUI 프로그램 실행

     


