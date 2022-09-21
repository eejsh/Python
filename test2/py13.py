#extent 형태의 파이썬 class

class box:          #box는 추상클래스형태
     def __init__(self,data1,data2):
          self.data1 = data1 
          self.data2 = data2

class box2(box):     #box2에서 box를 상속받음
     def __init__(self,data1, data2, data3): #상속 받을 때 인자값을 모두 가져옴
          box.__init__(self, data1, data2)   # 추상 클래스에서 셋팅된 self로 이관
          self.data3 = data3
     def abc(self):  #추상클래스 + box2 클래스값을 출력하게 됨(self)
          print("data값은 {0},{1},{2}"\
                .format(self.data1, self.data2, self.data3))

#box2를 호출해야만 box를 상속받아서 처리가 가능합니다.
a = box2("hong", "홍길동", "hong@hong,com")
a.abc() #box2에 있는 abc 메소드를 출력 하여 호출함

