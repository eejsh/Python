#편의성 및 함수이동 방법

# 은행 대기 순번  0001, 0002, 0003 ...


#for number in range(1,30):
#    print("대기번호 : " +  str(number).zfill(4))
  # zfill(숫자 자리수) : 자동으로 숫자 자리수를 맞추는 함수 입니다.
  
#숫자 3자리 마다 , 출력 ex)10,000,000,000
money = 10000000000 
print("{0:,}".format(money))

#함수이동
def abc():
     bbb()
     
     
def bbb():
    print("함수 이동으로 값을 출력시킴 ")      


abc()