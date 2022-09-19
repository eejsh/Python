'''
# 산술연산 기호 및 결과값 출력

print((10%3)) # 나머지 구하는 연산기호
print(10/3) # 소수점도 출력되는 나누기
print(10//3) # 소수점 절삭 후 출력 (정수로 출력)
print(2*3) # 곱하기
print(2**3) # 2^3 = 2*2*2


# 부등호 <, >, <=, >=, == !=, not
print(10+30 == 50)  #false 출력
print(10 != 20)   #true
print(not (10 != 20))  #false


print((10>5) and (4<5))  # true
print((10>5) and (4>5))  # false 앞 부등호는 맞으나 뒤 부등호가 틀림 -> false
print((10>5) & (4<5) ) # true  and==&
print((10>5) or (4>5)) # or 둘중에 하나가 맞으면 true
print((10<5) | (4>5))  # # false  or == |
'''

#여러ㅓ개를 한꺼번에 비교하며 전체가 모두 맞을 경우 true 출력, 그 외는 false
print(10>20>20) # false
print(3>2>1) # true

#괄호 부분에 포함한 산술연산부터 실행
print(10+20*10)  #210
print((10+20)*10) #300
num =(10+20)*10
print(num)

#증감, 감소, 곱셈, 나눗셈 연산형태 (+=, -=, *=, /=)
jum=5
jum+=4
print(jum)


