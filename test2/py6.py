#함수 def

def aaa():  #def라는 이름을 가지고 있으며 javascript function 와 비슷한 형태
     print("함수호출완료")

aaa()    # 함수를 즉시실행함


def bbb(a): #해당 함수에 인수값을 적용하여 출력함
     print("함수 호출 값은 {0}".format(a))
     
bbb("홍길동")


def ccc(b,c): #해당 함수를 이용하여 값을 계산 수 되돌려줌
     d = b + c 
     return d
z=ccc(5, 10)   #z 변수로 return된 값을 받음

print("결과 값은 {0} 입니다." .format(z))


money = 100000
def bank(umoney):
     if umoney > money : 
          msg = "출금하실 금액이 잔액보다 큽니다."
     else :
           m = money - umoney 
           msg = str(umoney) + "출금 되었습니다.  잔액은 " + str(m) + " 입니다."
     return msg
result = bank(5000)
print(result)


#함수 인수값에 값을 전달하여 출력하는 형태
def myinfo(username, age =33, email="hong@hong.com"):
     print("고객명 : {0} , 연령 : {1} , 이메일 : {2}".format(username, age, email))
 
myinfo("홍길동")     #username에 대한 인수값만 전달
#myinfo("홍길동", 30, "hong@hong.com")    
