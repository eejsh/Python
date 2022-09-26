import pandas as pd

#pandas pd로 명칭

#Series ▶ Time, Num, Data (간격에 맞춰서 배치된 데이터들의 값)
data = pd.Series([10,20,30,40]) 
#servies로 배열값을 로드 (인덱스값을 자동으로 설정함)
#print(data)

'''
일반print : [10,20,30,40.....

pandas print ( 시각화 )
0    10
1    20
2    30
3    40
dtype: int64

배열형식으로 인덱스 번호화 같이 프린트됨
'''
#index 기본숫자 (0부터 시작), index를 이용하면 데이터 인덱스 별명명칭을 적용할 수 있음
data2 = pd.Series([17,19,20,17,16,15,16], index = ['월','화','수','목','금','토','일'] )
#print(data2['월']) #지정된 index 별명을 출력할 수 있습니다. , 배열인덱스번호로도 출력가능 data2[0] == data2['월']


array = {
"username" : ['홍길동','이순신','강감찬'], 
"userage" : ['30','46','27'] ,    
"usercp" : ['skt','kt','kt']
}

# 일반 python 형태의 배열출력 ( key배열형태 )  
print(array) 
print(array['username'])



pr = pd.DataFrame(array) # dataframe을 이용해서 키가 있는 배열을 시각화 함
# pandas 로 시각화.. key가 목차역활을 하게됨
print(pr)

'''
  username userage usercp
0      홍길동      30    skt
1      이순신      46     kt
2      강감찬      27     kt
'''

print(pr['username'][2]) #key 값은 무조건 ",' 필요

# [['키이름','키이름']] : 원하는 키 값 이름만 데이터를 시각화 합니다. 
print(pr[['username','usercp']]) 
'''
  username usercp
0      홍길동    skt
1      이순신     kt
2      강감찬     kt
'''

#key 배열에 index 명을 바꿉니다.
pr1 = pd.DataFrame(array, index=['no1','no2','no3'])
print(pr1)
'''    username userage usercp
no1      홍길동      30    skt
no2      이순신      46     kt
no3      강감찬      27     kt
'''

#칼럼값을 위치 변경 (columns..)
pr2 = pd.DataFrame(array, columns=['usercp','username','userage'])
print(pr2)
'''
  usercp username userage
0    skt      홍길동      30
1     kt      이순신      46
2     kt      강감찬      27
'''


