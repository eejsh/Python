#파이썬 함수 + class, method

def aaa(a,b):
     print("상품명: {}, 가격:{}".format(a,b))
     print("함수출력")
     
aaa("가방", 6000) #함수호출


import defs as df

result = df.ccc()

print(result)
df.ddd(10, 20)


#-------------------class------------------------#


class cdatas : # 전역변수
     money = 5000
     def aaa(self):
         # global money 
         money = 1000 #지역변수
         #money 를 그냥 return 시 에러남 :  aaa 메소드에서 money 변수를 찾음.
         #return self.money : 전역변수값
         return money #지역변수값
         

cl = cdatas()
print(cl.money) # class 안에 여러개의 전역변수가 있으면, 해당 변수값을 바로 가져올 수 있음
result = cl.aaa()
print(result)

#-------------------외부class------------------------#

out = df.product()
out.add1(50000)
out.add3()

