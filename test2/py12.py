#class 선언 방식 및 메소드 형태

class box :  #class를 선언
     #_init_는 class 하나에 한번만 선언가능.
     def __init__(self, a, b, c): # _init_ class 호출 시 바로 실행되는 함수(public개념과 비슷함) #값을 받을때 숫자로만 받겠다고 선언. 
     #(DTO처럼 사용)
          self.a = a     # self : java(this)개념
          self.b = b
          self.c = c
          print("값은 {0},{1},{2}".format(self.a,self.b,self.c))
     
     def abc(self):  # 일반 메소드
          print(self.c)
          
box("고등어", "광어", 30)     #_init_ 에 인자값을 전달
box(50, 60, 70)

cl = box(5,10,15)   #_init_에 인자값을 전달하면서 setter 형태 
cl.abc() #abc 메소드를 로드하여 getter 형태


class box2:
     def __init__(self,name,id,pw):
          self.name = name
          self.id = id
          self.pw = pw
     def abc(self,email):      #일반 메소드에 추가 인자값을 적용
          print("고객명 :{0}, 아이디 : {1}, 이메일 : {2}" \
                .format(self.name, self.id, email))
          

data = box2("강감찬", "kang", "a123456")  #_init_에 값을 등록
data.abc("kang@kang.com")     #abc 메소드에 추가로 값을 등록


          
          
          