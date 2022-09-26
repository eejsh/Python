import pandas as pd 
data = pd.read_csv("area.csv", encoding='euc-kr')



#오름차순 sort_values
#print(data.sort_values("휘발유")) #휘발유 , 오름차순 

#내림차순 ascending=False
#print(data.sort_values("휘발유", ascending=False))
#print(data["경유"].sort_values(ascending=False))

#index 숫자값으로 내림차순
#print(data.sort_index())
#print(data.sort_index(ascending=False))

#print(pd.__version__)

#두개의 값을 내림차순 ( n가지 키값을 비교)
#print(data.sort_values(["휘발유","경유"],ascending=False))

#---------------------------------------------------------#

#모든 데이터 값 중 해당 문자값을 변경
#print(data["지역"].replace({"서울":"서울특별시","인천":"인천광역시"}))

#---------------------------------------------------------#
#기타문법
#print(data["지역"].str.upper()) #대문자
#print(data["지역"].str.lower()) #소문자

#---------------------------------------------------------#
#컬럼값을 추가하여 +,-,*,/ 등 산술연산으로 추가하는 방식 
data['평균값'] = (data['휘발유']+ data['LPG'] +data["경유"])/3
print(data)

#drop : 해당 컬럼값을 숨김 
print(data.drop(columns=["LPG"]))
print(data.drop(index=7)) # 해당 index 번호값을 숨김
