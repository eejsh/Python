#database 연결

from sqlite3 import *
from MySQLdb import *


con = connect(
     user = "",
     passwd ="",
     host ="",
     db = "",
     charset = "utf8" #sql 콘솔에서 \status 에서 언어패킷 확인 후 작성. utf-8 ? utf8, euc-kr.. 등 다를수있음 
     ) 
     
     
cur = connect.cursor()

sql = "select * from 테이블명 "

cur.execute(sql) #sql쿼리문 작성

#select 에서 fetchall함수를 이용하여 loop가 작동 되도록 함
for z in cur.fetchall():
     print(z)
     
     
delsql = "delete from 테이블명 where 고유컬럼명 = '값' "
cur.execute(delsql)

#insert, updata

insql ="insert into 테이블명 values(...)"
cur.execute(insql)
#데이터가 들어갔다가 지워짐(휘발성) commit 선언해줘야됨 
con.commit()

    