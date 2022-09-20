from random import *
# 반복문 + 조건문
array = [9, 12, 17, 22, 31]

'''
 # for 문과 if을 사용 시 들여쓰기를 주의 하셔야 합니다.    
for a in range(0, 30):
     if a in array:  # array[a]할 경우 인덱스값이 없는 부분도 있기 때문에 문법 오류 발생함
      continue  # 조건에 맞을 경우 ++가 적용되어 다음 반복문이 실행되도록 합니다.
      break # 해당 조건이 맞을 경우 반복문을 빠져나옴
     print(a)

for b in range(0,30):
  if b in array :   # 배열값과 반복되는 값이 같을 경우
        if b > 100 : # 그 외 100 이상이 될 경우 
             break  # 반복문 정지 
        else:       
             print(b)  #조건에 맞는 부분을 출력 
'''
                
w=0
while True :    # 무한loop 사용
 if w in array :
    if w<30 :
     print(w)
     w+=1     # 무한 loop에서는 w를 별도로 사용하지 않기 않으므로 +1 강제 증가시킴
 else :
    w+=1
    if w > 30 :  #무한 loop 이지만 30이상일 경우 강제종료
         print(w)
         break