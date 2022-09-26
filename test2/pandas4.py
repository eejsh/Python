# txt로 저장 
import pandas as pd

data = {
     "area" : ['강남구','강동구','강북구','강서구'],
     "gasoline" : [1947,1812,1677,1721],
     "diesel" : [1947,1918,1809,1855],
     "ev": [173.8,170,158.4,166]
     }

pr = pd.DataFrame(data)  #dataframe으로 로드.

#pr.to_csv("data.txt", encoding='euc-kr') #index번호 까지 저장함. 
#txt파일로 저장 , 콤마를 기준으로 저장됩니다.    index=False 선언 시 index번호 삭제 처리함
#pr.to_csv("data.txt", encoding='euc-kr', index=False)

# xls로 저장함
pr.to_excel("data.xlsx", index=False)

print(pr)



#https://pandas.pydata.org/
#https://pandas.pydata.org/docs/user_guide/io.html

#pip install xmwt
#pip install openpyxl 
#둘다 받아야 xlsx (excel) 파일 저장됨.


