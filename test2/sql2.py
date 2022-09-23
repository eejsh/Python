from sqlite3 import * 
from dbconnect import * 
from random import *
from distutils.dist import command_re
from MySQLdb.constants.FLAG import AUTO_INCREMENT
from MySQLdb.constants.FIELD_TYPE import VARCHAR

#[42,43,44]

'''
#수정(update)
for a in range(42,45): # sql 에 index 고유값에 대한 범위를 선정
     cur = connect.cursor()
     sql = "update test3 set mpw= 'a123456' where midx='"+ str(a) + "'";
     #해당 index값을 모두 변경이 되도록 반복시킴
     #%s 사용시 sql문법 전체를 %s 로 적용해야만 정상적으로 반영이 됨.
     
     cur.execute(sql)
     connect.commit()
'''

#삭제
#cur = connect.cursor()
#for b in range(42,45):
#     sql ="delete from test3 where midx = '"+str(b)+"'"
#     cur.execute(sql)
#     connect.commit()


#신규테이블 생성
cur = connect.cursor()
sql = "create table shopping(sidx int(4) not null AUTO_INCREMENT, sname VARCHAR(100) not null, primary key (sidx))"
cur.execute(sql)
connect.commit()