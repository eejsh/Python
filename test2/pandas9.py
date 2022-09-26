import pandas as pd
from sqlite3 import *
from dbconnect import *

sqlin = connect.cursor()
#pandas db 연결
sql = "select * from test3"

#read_sql_query , read_sql : pandas 전용 DB 연결 형태
#read_sql_query ("sql 문법", "DB접속정보")
data = pd.read_sql_query(sql, connect)


#삭제 형태로 가져오는 컬럼 형태
#data = data.drop(columns=["midx","mpw","mtel"]) #pw는 출력하면 절대안됨!!


#저장할 컬럼만 가져오는 형태
data = data[["mid", "mnm", "mage"]]
data = pd.DataFrame(data)
data = data.rename(columns={"mid":"아이디", "mnm":"이름", "mage":"나이"})
#r : 기존에 있는 데이터를 삭제하고 새롭게 저장할 수 있도록 사용하는 속성값
data.to_csv(r"test3.csv", encoding='euc-kr') #csv 로 저장


#필요한 컬럼 가져옴
#data = data[["mid", "mnm", "mage"]]
#print(data)
