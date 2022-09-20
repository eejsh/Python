##파일저장
from idlelib.iomenu import encoding

# open("파일명","읽기, 쓰기 (w)","언어셋" ) : 파일 생성 및 저장
#해당 파일 생성 및 쓰기 
files = open("./data.txt", "w" , encoding="utf-8")
print("홍길동", file = files)  # file = 해당 파일명에 데이터를 저장
print("이순신", file = files)
files.close()   #open된 파일을 close로 종료


# 해당 파일을 수정
files = open("./data.txt", "a" , encoding="utf-8")
print("유관순", file=files)
files.close()

#해당 파일을 읽음
files = open("./data.txt", "r", encoding="utf-8")
#print(files.read())
#print(files.readline()) #데이터를 한줄씩 읽어서 오는 함수

'''

#반복문으로 파일에 문자값을 가져옴
while True :
     line = files.readline() # 파일에 있는 라인별로 읽어옴
     if not line :   #만약에 더 이상 읽을 라인이 없을 경우.. 
          break
     print(line, end="") # end="" , readline은 엔터기능 없앰(공백제거)
files.close()
#end 는 출력 마지막에 적용할 문자, 숫자를 표기 할 수 있습니다.
print("홍길동", end="2500")
'''

#python은 while문 보다 for in이 더 좋음..

for line in files.readlines():  #readlines 이용해서 반복문 출력
     print(line, end="")
files.close()    
