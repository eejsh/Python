#예외처리 try~ except

try :  #정상 처리
     a = "1231"
     #a = "홍길동"
     b = int(a)
     print(b)
         
except : #예외처리 
     print("error")        
finally :
     print("모든 정상처리가 완료되었습니다.  ")     