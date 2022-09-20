#전역변수, 지역변수

box ="변수값"
box3 =""        #최초 전역변수값에 비어있는 값


#전역변수는 절대 값이 변화가 없음.. 단, global 사용 시 작동가능 (static과 비슷한 역활)
def afunction():
     global box3 # 전역변수명을 호출 함 . (jsp, php, c등 사용)
      
     print(box)
     box2 ="변수값2"
     print(box2)
     print(box3) #전역변수값이 출력
     #만약에 global 이 없을 경우 새로운 지역변수가 생성되며, global 적용 시 전역변우세 새로운 값을 적용하게 됩니다.
     
     box3 ="변수값3"  #afunction실행 시 box3 에 문자값이 입력됨
          

def bfunction():   
     print(box)
    # print(box2) : error! afunction에서 사용하는 변수를 bfunction에선 사용하지 못함 box2없음
     print(box3)    #a값 출력됨
     #단, afunction보다 bfunction이 먼저 실행 될 경우 값이 box3은 빈값 출력
     
afunction()
bfunction()     