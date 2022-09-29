#복습 1 (python)

# 기본 무조건 배열

'''
파이썬 웹 서버 구축? 
flask는 보조장치임
java 에디터랑 python 에디터 구분하여 사용 추천 : 이클립스 자바 설치 되어있음 다른 에디터 사용추천함  (error 피하기)

개발도구 : 파이썬 설치 3.11 
파이선 설치 시 런처에서 add python 3.11 to path 체크 해야 에이터에서 파이선 자동으로 찾음! 꼭 체크해야됨

그 외의 패키지 - pip install 패키지 명
패키지 삭제 - pip uninstall 패키지 명  (통신불안정이나 error시 삭제 시 사용)


파이썬 변수에 자료형 없음, object 형태 .. str, int로 변환해서 사용해야됨.(var, string 필요없음..)


for in (배열데이터), while(일반 반복문)
보통 for in을 사용함.

'''
abc= ["a","b","c", 10]
print(abc)
print("{}".format(abc[0])) #배열데이터 개당 값 출력 할때 사용.

#랜덤 
import random as rd  #java, c 사용자들은 import as rd 가 편할수도있음..
aaa=rd.randint(4,10)
print(aaa)

from random import*
bbb = randint(5,10)
print(bbb)

'''주석처리, msg선언시 문자열로 사용가능.'''
#문자열
msg = """
[이용안내]
안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요
"""
print(msg)

hp = "010-1234-5678"
print(hp[9]) # 5출력. 파이선은 기본 배열로 인식됨 원하는 문자열 찍고싶으면 배열[index]로 출력해야됨. 
print(hp[0:3]) #010
print(hp[:7]) #해당 문자열부터 ~7까지 문자열
print(hp[8:]) #해당 문자열부터 ~ 끝까지
print(len(hp)) #문자열에 대한 갯수 length..
print(hp.replace("-", ""))
print(hp.find("1234")) #출력값4, 4자리 부터 있음 //html 태그 찾을 때 많이 사용함.  indexof랑 비슷..

#findall 은 변수로 받아서 배열로 처리함, findall은 re패키지 import해서 사용해야됨!
import re as r
array = r.findall("1", hp)
print(array)


#변수값 출력
abox = 3000
cbox = 5000
total = f"{abox} 와 {cbox} 부분 금액 입니다." #{값} 사용 시 f 붙여줘야됨. 
print(total)

#경로 출력
#print("c:\program\python1\") #일반 문자로 출력






