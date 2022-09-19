#절대값을 구하기
'''
print(abs(-100)) #음수를 양수로 무조건 변경
print(pow(2,3)) # 2^3 , 제곱근을 표히

print(max(10,8)) # 여러개의 값 중 가장 큰 값을 가져올 때
print(min(5,9)) # 여러개의 값 중 가장 작은 값을 가져올 때

#abs는 배열 형태로 수정 후 양수로 변경이 가능합니다. 그 외의 방식은 사용하지 않음
#max, min 의 경우는 배열을 사용하지 않아도 숫자를 나열할 경우 큰 값, 작은값을 가져옴

print(max(1,-5,8,-7,11,3,-6))

# round : 반올림 0.5 단위
print(round(3.74)) #4
print(round(3.11)) #3


# round 외에 모듈을 사용하는 경우 (floor, ceil)
#import 방식은 두가지. from math import (단 문법에 별도 math 선언 없어도됨.), import math

from math import *   # 문법에 math 없이 사용하는 방식
print(floor(3.74)) #3
print(ceil(3.74)) #4

import math  # math모듈을 가져옴.
print(math.floor(3.74)) #3 해당 모듈에 따른 이름을 선언하고, 문법을 사용함.
print(math.ceil(3.74)) #4
'''

from random import*
print(random())
print(random()* 10) # 소숫점 포함하여 임의값 생성
print(int(random()*10)+1) # 0~10 미만의 임의값 생성
print(randrange(1,11)) # 1~10미만 (1~9) 의 임의값 생성 randrange로 바로 범위값 잡아 사용가능

print(randint(1, 2))  # 1~2까지 임의 숫자 생성

#문자열을 출력하는 방식 ''' 또는 """ 으로 사용하게 됩니다.

msg ='''홍길동님 환영합니다.
적립금은 2500원 사용하실 수 있습니다.'''

print(msg)
