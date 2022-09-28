 #양극 형태의 그래프 형태 만들기. 
import pandas as pd
import matplotlib.pyplot as mpt
import mfont

#csv 형태로 시트 셀 읽기
#data = pd.read_csv("person.csv", encoding="euc-kr",usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])

#xls 로 구성 시 usecols='셀' 범위

                                 
#총인구수                             usecols="A,B,D:X"
data = pd.read_excel("person.xlsx", usecols="D:X")

#남자인구수
man = pd.read_excel("person.xlsx", usecols="AA:AU")


#여자
woman = pd.read_excel("person.xlsx", usecols="AX:BR")




#iloc : 행 번호에 맞춰서 해당 행에 있는 모든 데이터를 가져오는 함수입니다. 
#iloc(xls, xlsx) 엑셀에서 사용함. csv는 error

#print(data.iloc[1])


#(data.columns) : 컬럼 이름만 배열로 출력함 
#print(data.columns)


#print(type(data.iloc[0])) #<class 'pandas.core.series.Series'>
'''
a_data = data.iloc[0]
mpt.figure(figsize=(10,5))  #figure 그래프 이미지 x,y 늘려줌
mpt.barh(data.columns, a_data//1000) #1000명 단위로 출력 
'''
m_data = man.iloc[0] #man.columns 목차
w_data = woman.iloc[0] #woman.cloumns 목자

mpt.figure(figsize=(10,8))
mpt.barh(data.columns, -m_data//1000, label="남성인구") #남 데이터
mpt.barh(data.columns, w_data//1000, label="여성인구") #여 데이터 
mpt.legend()

mpt.title("2022년 8월 남여 인구 분포도")
mpt.savefig("202208person.png",dpi=200)
mpt.show()

