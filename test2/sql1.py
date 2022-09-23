from sqlite3 import * 

from dbconnect import *  #connect py파일 별도로 만들어서 로드해서 사용함.

#python sql :  pysqlite3, pysqlite2,  sqlite3

#pip install pysqlit3
#pip install mysqlclient

#cousor : sql의 커서..

cur = connect.cursor()  #명령어를 입력시키기 위한 대기상태
cur.execute("select * from test3") #execute : sql 콘솔상태에 문자값을 입력..

for a in cur.fetchall():   
         #fetch all : select에 대한 데이터를 문자열 형태로 가져옴  (mysql_fetch_arrry()) 
     print(a)


#cur.execute("insert into test3 values ('0', 'king', 'abab12', '긩긩깅', '01012345678', '40');")

#java에서 ?를 이용하여 sql 에 사용하는 statement와 비슷한 구조형태를 가집니다.

cur = connect.cursor()
sql = "insert into test3 values ('0',%s, %s, %s, %s, %s)"

#with 를 이용하여 여러개의 데이터를 한꺼번에 저장, 수정, 삭제를 할 수 있습니다.
with connect :
     cur.execute(sql, ("red","red1234","레드사용자","01022223333", "50"))
     cur.execute(sql, ("blue","blue1212","블루사용자","0107878454","44"))
     cur.execute(sql, ("orange","orange0111","오렝지사용자","01078956125","56"))
     connect.commit()
     
#insert, delete, update는 commit이 필수..
#commit()을 사용해야 하는 이유? : insert 후 delete를 바로 해버리는 파이썬 특유의 행동 부분입니다.




'''
create = con.cursor()
create.execute("create table test( idx int(4) not null , name varchar(200) not null,primary key(idx))")

insert = con.cursor()
insert.execute("insert into test values ('0', 'hong');")
'''