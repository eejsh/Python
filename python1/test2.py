username="홍길동"
msg = "적립금"
point =5
money1 = 1000
money2 = 2000
money = money1 + money2


''' str(변수명) : 숫자를 바로 print로 적용하지 못합니다. 
해당숫자를 문자화 시켜서 출력하셔야 합니다.
'''

print(username + " 님 환영합니다.")
print(username + " 님 "+ msg +"3000원을 사용하셨습니다. ")
msg = "포인트"
print(username + " 님 "+ msg +"은 " +str(money)+ "원 입니다.")
print("고객님은 현재 골드회원이며, "+msg+"은 "+str(point)+"% 적립 됩니다.")