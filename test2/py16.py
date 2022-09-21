#특정 예외처리 구성

try:
     print("두개의 값을 입력하세요")
     data = []
     number1 = int(input("첫번재 숫자를 입력하세요."))
     number2 = int(input("첫번재 숫자를 입력하세요."))
     
     if number1 >=1 and number2 >= number1 :
          data.append(number1)
          data.append(number2)
     
     else : 
          raise OverflowError  
     #raise : 해당 이름을 가진 except를 선정하여 실행되도록 함.
          
     print(data)


except OverflowError:
     print("두번재 숫자 입력 시 첫번째 숫자보다 크게 입력하세요.  ")

except ValueError : #error가 되었을 때 적용되는 부분 
     print("숫자만 입력하세요. ")
     
finally:
     print("모든 프로세서가 종료 됩니다. ")     
   
     
     
     