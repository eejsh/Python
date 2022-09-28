import pandas as pd
import matplotlib.pyplot as mpt
import mfont

#data=[1,1,1,1,1,1]
data = [30,25,20,17,10,6]
text = ["1일차","2일차","3일차","4일차","5일차","6일차"]
color= ["red","blue","green","pink","orange","skyblue"]

#explode 기본 형태로 설정 시 사용
#transform = [0.2,0.1,0.1,0,0,0]    #원그래프 변형하기 위한 배열

#원 그래프에 배열 갯수에 맞춰서 모두 분리.  (배열의 개수는 무조건 맞춰야됨 error남..)
transform = [0.05] * 6



#autopct : 1개의 데이터 당 %로 구분자를 두는 함수
#1f : 소수점 1자리, f:flot . '%.1f%%' =1개 소숫자리, '%.2f%%' 소수점2자리.. 
#1i : int
#%% : 그래프에 %를 출력 하기 위한 표시
#startangle : 원에 대한 각도 조절

#원 그래프 기본 형태
#mpt.pie(data, labels =text, autopct='%.1f%%', startangle=45) #%%는 두번,,


#원 그래프 변형 형태
mpt.pie(data, labels=text, autopct='%.1f%%', explode=transform, colors=color)
#explode : 원 그래프에 대한 조각을 별도로 분리하는 형태 (explode... java에서 단어분리때 사용.. )
mpt.title("원 그래프 테스트")
mpt.legend(loc = (1, 0.5)) #목차 loc (위치 변경) → loc(X축, Y축) 
mpt.show()

