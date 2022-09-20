#if 조건문

'''
a = 10
if a == 5 :     #if문 : = {}
    print("숫자 5 입니다.")
elif a==10 :    #elif문 : else if
    print("숫자 10 입니다.")
else:
    print("숫자 15 입니다.")
    
#input = java Scanner 기능
b = input("좋아하는 숫자를 입력하세요?") 
c = int(b)%2  # input에 입력된 값은 모두 str 로 인식하므로 int로 변환 해야 산술식이 적용됨 
if c==0 :
    print("해당 숫자는 짝수를 입력하셨습니다.")
else :
    print("해당 숫자는 홀수를 입력하셨습니다.")


person = input("고객 아이디를 입력하세요")
if person == "hong" or person == "kim":
    print("일반 회원입니다.")
elif person == "park":
     print("실버 회원입니다.")
else:
    print("가입되지 않은 회원입니다.")
'''
    
#사용자가 입력한 값을 숫자로 자료형 형변환을 할 경우     
number = int(input("총 입금하실 금액은?"))
if 10000 > number :
    print("입금은 최소 10000원 이상 입력을 하셔야 합니다.")
#elif number >= 10000 and 5000000 >= number :
elif 10000 <= number <=5000000 :       # 입력범위를 설정하여 조건에 맞는 결과 출력 
    print("정상적으로 입금이 완료되었습니다.")   
else :
    print("입금은 한번에 5000000원 까지 입니다. ")