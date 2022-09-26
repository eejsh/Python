import pandas as pd 
data = pd.read_csv("area.csv", encoding='euc-kr')

#print(data["휘발유"])
#print(data["휘발유"]<=1700)
#조건 출력문 true, false로 합격 .. pandas전용, 숫자위주로 사용

#filter : 변수에 조건을 적용하고 해당 조건을 배열키로 적용하여 필터링 하게 됩니다.
aa_filter  = (data["휘발유"]<1700)
#print(data[aa_filter]) # 1700이상 출력
#print(data[~aa_filter])#~170이상 ~(반대)
#print(data[~aa_filter],["휘발유"])

# &, | 를 이용하여 두 조건이 만족하는 사항에서 데이터를 출력
filter2 = data.loc[(data["휘발유"]<=7000) & (data["지역"]=="대구")]
#print(filter2)

filter3 = data.loc[(data["휘발유"]<=1700) & (data["경유"] <= 1800)] # 휘발유, 경유 두조건이 맞는 지역? = 대구..
filter4 = data.loc[(data["휘발유"]<=1700) | (data["경유"] <= 1800)] # 휘발유, 경유 두조건이 맞는 지역? = 대구..
print(filter3) # and 모두 맞을시
print(filter4) # or 둘중 하라도 맞을 시

