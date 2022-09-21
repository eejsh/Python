#다중 상속(java implements)


class box :  #첫번째 상속
     def __init__(self,data1):
          self.data1 = data1 

class box2 : #두번째 상속
     def __init__(self,data2):
          self.data2 = data2 


class box3(box, box2): #다중상속 이용 box, box2 로드
     def __init__(self,data1 , data2, data3):
          self.data3 = data3  #box3 에 대한 값을 self로 이관
          box.__init__(self, data1)  #상속값을 return
          box2.__init__(self, data2) #상속값을 return
          print("데이터값 {0},{1},{2}"\
                 .format(self.data1, self.data2, self.data3))


a = box3("홍길동", "강감찬", "이순신")  #인자값을 box3으로 보냄
print(a)        