from random import* #random 라이브러리(random, randrange, randint < range(여러개..)

#set, list
user = range(1,20) # 1~20까지 데이터 생성
#range는 배열 범위 데이터를 생성하는 클래스 입니다.

user = list(user)
#range사용시 set 또는 list 로 재구성 해주셔야 합니다.

print(user) # 1~20까지 순차적으로 출력함

shuffle(user) # 배열값을 랜덤하게 순서를 변화시킴
print(user)
#random → sample 1개 이상 값을 가져올때 사용.

lotto = sample(user, 6) # sample(배열명, 갯수) 랜덤하게 갯수만큼 숫자를 가져옴
print(lotto)

print("1등 당첨번호 :" + str(lotto[0]))
print("1등 당첨번호 :  {0}".format(lotto[0]))
print(("보조 당첨번호 : {0}".format(lotto[1:])))