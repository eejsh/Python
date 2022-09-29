# 함수 전용 파일

def ccc():
     return "test"

def ddd(a, b):
     c=a+b
     print(c)
     
     
gdata ="핸드백" #전역변수

class product:
     data1 = "가방"
     data2 = "휴대폰"
     
     def add1(self, m): #rev4에서 50000 값 m으로 받음
          global gdata #global을 선언 시 전역변수을 호출함. 
          #global 호출 시 gdata 번역변수가 됩니다. 
          result = self.add2(m)
          gdata = "바지"  # 지역변수 gdata (global 선언X : 지역변수 바지로 출력)
          print(result)
          print(gdata)
     def add3(self):
          print(gdata)    
          
          
     def add2(self,mm): #mm = 15줄 self.add2(m에서 받음)
          data3 = self.data1 + "금액은 " +str(mm)
          return data3
     