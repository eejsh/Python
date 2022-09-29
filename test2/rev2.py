#배열 형태의 데이터 {} []
a=10
b=20
c=30

array = [a,b,c]
print(array)

adata1 = [1,2,3]
adata2 = [100,200,300]

adata3 = [adata1 , adata2]

#extexd 사용 시 신규 변수를 생성할 필요 없이 기존에 있는 상속된 변수를 출력하면 됩니다.
adata1.extend(adata2) #adata1에 adata2를 상속시킴.

print(adata3)
print(adata1)

#---------------------------------------------------------------------------#

zdata1 = {1,2,3,4}
zdata2 = {"key1":"홍길동", "key2":"이순신"}
print(zdata1)
print(zdata2["key1"]) #홍길동 출력
print(zdata2)

#----------------------------------------------------------------------------#
kdata1 = {"kdata": [1,2,3], "jdata": [100,200,300]}
print(kdata1["kdata"]) #1,2,3
print(kdata1.get("kdata")) #key 가 있을 시 get 사용으로 출력할 수 있음
# print(kdata1["kdata"].get(1)) ---error! 자바 출력형태임

print(kdata1.keys())  #키값 .  pandas 컬럼명 필요할때 사용됨
print(kdata1.values()) #배열값

#----------------------------------------------------------------------------#

person = ("홍길동", "이순신") #파이썬에만 있는 배열 구조형태
print(person[1])

(aa,bb,cc) = ("a1", "b1", "c1")
print(aa)



 