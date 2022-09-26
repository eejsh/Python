#csv 저장 and 읽기 
import pandas as pd
from idlelib.iomenu import encoding
data = {
     "area" : ['강남구','강동구','강북구','강서구'],
     "gasoline" : [1947,1812,1677,1721],
     "diesel" : [1947,1918,1809,1855],
     "ev": [173.8,170,158.4,166]
     
     }

#csv 생성 시 dataframe을 무조건 선언 후 저장 합니다.
pr = pd.DataFrame(data)
pr.index.name="유가리스트"

#to_csv는 csv 파일로 저장하는 함수(판다스 전용 문법)
pr.to_csv('opinet.csv', encoding='euc-kr') #encoding : csv 파일은 기본으로 euc-kr 사용. (ansi,, utf-8은꺠짐)
#print(pr)

#csv 파일 로드 (읽기) 기본 encoding= euc-kr로 설정 
#skiprows : 1번째 줄 삭제 후 출력
data2 = pd.read_csv('ori.csv', encoding='euc-kr', skiprows = 1) 
print(data2)
