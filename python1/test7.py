#배열
age = [10,20,30,40,50,60,70,80,90,100]
print(age[2])

person =["홍길동", "이순신", "강감찬"]
print(person[2])

print(person.index("강감찬"))  # index 배열에 몇 번째 노드에 있는지 확인
print(len(person)) # 배열 총 갯수

person.append("유관순")
print(person)

person.insert(1, "세종대왕") # insert 배열값에 원하는 위치에 값을 적용할 경우
#insert(노드번호, 추가할 값)
print(person)

print(person.pop()) #유관순 pop() 값을 맨 뒤에서부터 차례대로 가져오게됨
print(person.pop()) #강감찬..


numbers =[5,8,7,1,9,3,2,6]
numbers.sort()   # 오름차순으로 배열나열
print(numbers)
numbers.reverse() #내림차순으로 배열나열
print(numbers)

numbers.clear() # clear : 값을 비움 [빈배열]
print(numbers)

datas = ["hong", "홍길동", 33, 3000, False]
datas2 = ["면도기", "신발", "바지", "이어폰"]

#datas에 있는 배열값과 datas2 에 있는 배열값을 datas에 종속시킴. 
datas.extend(datas2) #단, 배열값을 종속 시킬 때는 변수로 받아서 처리하지 않습니다.
print(datas) #해당 배열 변수명을 출력

#키 값이 있는 배열형태
infodata = {"mid":"hong", "mname":"홍길동", "age":33}
print(infodata["mname"])   # 배열에 있는 키명으로 로드
print(infodata.get("mid")) # get이라는 함수 이용해서 키 배열값을 가져오는 형태

# in은 키배열에 해당 키명이 있는지를 확인할 때 사용하는 문법입니다. 
print("age" in infodata) # true
print("mtel" in infodata) #false

#ket배열에는 append, insert라는 문법을 사용하지 않고 입력, 수정 하실 수 있습니다.
infodata["tel"] = "01023456789"
print(infodata)
infodata["age"] = 30
print(infodata)

#키배열값 삭제
infodata["mid"] = "" #key값은 그대로, 데이터만 삭제
#del infodata["mid"] #아이디 데이터 삭제.
print(infodata)

infodata.keys()
print(infodata.keys()) #키 이름만 출력 =Object.keys(Javascript) 
print(infodata.values()) # 키 배열에 값만 출력할 경우
