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
mpt.Figure(figsize=(10,8))

titles = data.columns;  #0~4세, 5~0세.. 컬럼값
mandata = man.loc[0] #데이터를 한개만 들고오기 . bar 데이터 인식문제로 1개만.. 
mpt.bar(data.columns, man.loc[0])

#plot 그래프
mpt.plot(data.columns, woman.loc[0], color="red")


mpt.show()