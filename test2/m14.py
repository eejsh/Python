import pandas as pd
import matplotlib.pyplot as mpt
import mfont
import numpy as no  #numpy : 산술 형태의 패키지


data = pd.read_csv("area.csv", encoding="euc-kr")

f,axes = mpt.subplots(2,2,figsize=(15,15))
f.suptitle("각 지역별 유류가격 데이터 ")

#첫번째
axes[0,0].bar(data['지역'], data['휘발유'], label='휘발유')
axes[0,0].set_title("지역별 휘발유 가격비교")
axes[0,0].set_facecolor('pink') #배경색
axes[0,0].legend()

#두번째
axes[0,1].plot(data['지역'], data['경유'], label='경유', marker='*')
axes[0,1].set_title("지역별 경유 가격비교")
axes[0,1].set_facecolor('yellowgreen') #배경색
axes[0,1].legend()

#세번째
axes[1,0].barh(data['지역'], data['LPG'], label='LPG')
axes[1,0].set_title("지역별 LPG 가격비교")
axes[1,0].set_facecolor('skyblue') #배경색
axes[1,0].legend()

#네번째
area = data["지역"];
#no.random : numpy 전용 랜덤
#rand(생성갯수)
sizes = no.random.rand(len(area))*1000
print(sizes)
axes[1,1].scatter(data["휘발유"], data["LPG"], s=sizes)
axes[1,1].set_title("분석값")


mpt.show()