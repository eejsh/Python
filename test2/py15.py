#사용자 입력값에 따른 결과 출력 (예외처리 하는 방식)

try:
     print("두개의 값을 입력하세요")
     data = [] #빈배열
     data.append(int(input("첫번째 숫자를 입력하세요.")))
     data.append(int(input("두번째 숫자를 입력하세요.")))
     print(data)

   
#except ValueError : #error가 되었을 때 적용되는 부분 
#     print("숫자만 입력하세요. ")
     
     
except : #java에서 사용하는 기본 Exception 입니다.  
     print("전체적으로 오류가 발생할 경우 ")