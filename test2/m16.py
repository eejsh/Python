#그래프 형태 2가지 사용 시 데이터 컬럼 갯수가 같아야 함

import pandas as pd
import matplotlib.pyplot as mpt
import mfont


#총인구수
data = pd.read_excel("person.xlsx", usecols="D:G")

#남자인구수
man = pd.read_excel("person.xlsx", usecols="AA:AD")

#여자
woman = pd.read_excel("person.xlsx", usecols="AX:BA")

#data.T or data : index에 대한 위치가 변경됨
#print(data.T)
#print(data.columns)


#여러 데이터 중 한개만 사용하는 사항 (여러 데이터 출력 시 bar 그래프가 올바르게 반영되지않음)

#bar 그래프 (남자데이터)
#subplots, subplot : 한개의 그래프에 여러 데이터를 보여줄 경우 사용 


#subplots로 사용하면 데이터 n개로 나오고, subplot을 두번 선언 시 2개 출력됨.(0,1,1)은 좌표 
#ex)mpt.subplot(0,1,1) .. 
#   mpt.subplot(0,1,2)

 
fig, ax1 =  mpt.subplots(figsize=(10,8))
titles = data.columns;  #0~4세, 5~0세.. 컬럼값
mandata = man.loc[0]//100  # //(단위숫자가 만단위가 넘어갈 경우 숫자 나누기)
#데이터를 한개만 들고오기 . bar 데이터 인식문제로 1개만.. 

ax1.bar(data.columns, mandata, color="skyblue", label="남자")
ax1.set_ylim(0, 30000) # 세로 데이터의 최대치 값
ax1.set_ylabel("남성 0~19세 인구수") #왼쪽 데이터 표에 대한 설명
ax1.legend()   
#반복문으로 해당 값을 그래프 위에 출력


for idx, txt in enumerate(mandata):
     ax1.text(idx, txt+500, format(txt,','),ha='center')

#ax1 = 바탕표라고생각하면됨. ax2가 겹쳐진거라 mpt으로 할 경우 뒤에 데이터가 안보일수있음!


#plot 그래프 (여자데이터)
#바 그래프가 남성 데이터와 겹치지 않도록 하기 위함. 
womandata = woman.loc[0]//50
#twinx, twiny
#그래프에 수치값 표현시 주의점? : 값을 나누어서 표현할 경우 +1, +10 은 표현이 안됨 좀더 많은 숫자를 입력해야만 적용됩니다. ( 나눈값이 수치값보다 커서..) 
#  ax1에서 컬럼값으로 했으니 ax2도 동일하게 data.column 값으로 설정!
ax2  = ax1.twinx() #그래프 데이터에 추가로 별도의 수치값을 표현 (ax1에 대한 수치 포함/보조개념)겹쳐짐 label이 겹쳐서 나올수있음.
ax2.set_ylim(0,30000)
ax2.set_ylabel("여성 0~19세 인구수")
ax2 = mpt.plot(data.columns, womandata, color="pink", marker='o', label="여자")

#그래프 출력? 1e6? : (10만 단위)  단위가 넘어가서..

#선 그래프에 해당 수치값을 표현
for idx2, txt2 in enumerate(womandata):
     mpt.text(idx2, txt2+500, format(txt2, ','), ha='center')


mpt.legend(loc='center left')
mpt.show()

