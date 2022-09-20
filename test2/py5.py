#python으로 다음과 같이 출력되는 코드를 작성하시오.
# 2*1 ~ 3*9 까지 출력
# hit range, for in

'''
from random import*
for a in range(2,4) :
  for b in range(1,10) :
        print( str(a) +"*"+ str(b) +"="+ str(a*b))
'''

data = [2,6,7,3,1]
print(data)

data =[i+1000 for i in data]# 배열값에 기존 배열값을 적용하여 산술식으로 배열을 새롭게 구성함
#반복문 돌아가면서 기존 배열에 원하는 값을 추가적용
print(data)


#다양한 형태로 배열값을 반복문을 통해 변화시킬 수 있습니다. 
person = ["kim", "park", "lee"]
#person = [aa.upper() for aa in person]
person = [aa.replace("k","j") for aa in person]
print(person)

#사용예시 :010-1234-5678, 01022233445 , 010.2234.4567...
