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
mpt.Figure(figsize=(10,8))

w1 = 
mpt.plot(man//1000, data.index,  marker='o')
w2 = 
mpt.plot(woman//1000, data.index, marker='*')

mpt.show()