#파이썬 배열 선언시 중요사항
from cffi import api

adata ={10,5,6,7,6,3,10,6} # {} 선언 배열은 중복된 값 삭제 
print(adata)
adata2 = [10,5,3,7,6,3,10,6] # [] 배열 시 모든 값 출력
print(adata2)

'''
#배열 값을 반복문으로 가져오는 형태 
for no in adata2 :
     print(no)     


# for문 배열 형태2
adata3 = {"data1":[1,2,3,4], "data2" :["5","6","7","8"]}
for k in adata3:
     print(k) #key값만 나옴
     
     for kk in adata3[k] :
          print(kk) # 값 출력
'''

#for문 배열 형태 3 (enumerate) 
adata4 = [100,200,300,400,500]
  #인덱스번호, 배열의 값
#for idx, no in enumerate(adata4) : # enumerate: 인덱스, 배열값 을 분할하여 사용할수 있음
#     print(no) 
#     print(adata4[idx])         
     

#while문 ------------------------------------------------------#
w=0
while w <= 5:
     if w==2 :
       print(w)
       break   #continue : 반복 순서를 넘기는 형태
              #break : 반복문 정지  
     w+=1   # ++, -- 없음. +=(1식 증가), -=(1식 감소) 사용!     

while w<5:
     print("배고파")
     w+=1
