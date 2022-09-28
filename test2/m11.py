#빅데이터 분석 차트 형태

import pandas as pd
import matplotlib.pyplot as mpt
import mfont

data = [120, 50, 180, 97, 165]
data2 = [50,75,95,42,16]


#해당 값에 대한 크기를 표시하기 위한 배열값
total = [data[0]+data2[0],data[1]+data2[1],data[2]+data2[2],data[3]+data2[3],data[4]+data2[4]]
#scatter : 산점도 그래프 (빅데이터 분석표로 많이 활용함)
#산점도 그래프는 무조건 sizes를 정해서 출력하게 됩니다. , 원의 크기 사이즈로 잡아서 출력함. 


#별도데이터
cdata = ["red","blue","green","orange","gray"] 
data3 = ["서울", "경기", "세종시", "광주", "대구"]


#amap 대신 colors 배열 설정해서 사용해도됨..

#scatter 에 반복문을 이용해서 text값을 출력시킴
#mpt.scatter(data, data2, sizes=total)
for a, textin in enumerate(data3):
   mpt.scatter(data, data2, sizes=total, c=total, label=data3[a]) 
   mpt.text(data[a]-5, data2[a]+3, data3[a], color=cdata[a])
   
#칼라로 색상바를 표현하는 형태 (ex:주로 날씨..)
# orientation :세로
mpt.colorbar(orientation="horizontal")
mpt.title("각 지역별 차량보유대수 ")
mpt.xlabel("휘발유 차량")
mpt.ylabel("경유 차량")
mpt.show()