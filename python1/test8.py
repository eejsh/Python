# 배열기호, [],{}   
#튜플 : 셀수 있는 수량의 순서가 나열된 형태
'''
subject =("자바", "파이썬", "서블렛")
print(subject[1])

a1="홍길동"
a2 =" hong@cate.com"
a3 ="N"
a4 = (a1,a2,a3)
print(a4)


#세트(집합) : 중복된 데이터는 출력이 되지 않도록 합니다.
listdata ={100,200,300,200,100,600,700}
print(listdata)

listdata2 = {"홍길동","이순신","홍길동","강감찬"}
print(listdata2)

#[] 로 시작하는 배열형태는 중복 데이터가 있어도 모든 값이 출력됩니다. 
listdata3 =[100,200,300,200,600,200,500] #append, insert

##주의사항이 필요함..
listdata6 = set([100,200,300,200,600,500]) #set을 적용 시 [] => {} 인식시킴
listdata6.add(800)
listdata6.remove(200)
print(listdata6)


listdata3_1 = {100,200,300,200,600,200,500}
listdata4 = set([300,700])  # set : 교집합 형태 , 교집합 형태 주의할점 : 비교배열은 {}, set은 []으로 표현 
#중복 값중 뽑고 싶은 값 (listdata4)

print(listdata3_1 & listdata4) # &3_1 과 4 배열 중 4번 배열을 기준으로 3_1의 값을 가져옴
print(listdata3_1.intersection(listdata4)) #intersection 가 & 기호로 대체 되었음


print(listdata3_1 | listdata4) #합집함
print(listdata3_1.union(listdata4)) #union | 기호로 대체되었음

print(listdata3_1 - listdata4) # 차집합 
print(listdata3_1.difference(listdata4)) # difference : 기호로 대체되었음..

'''


#type == typeOf와 동일한 기능

box = {"블랙커피","아메리카노"}  
box2 = ["블랙커피", "아메리카노"]
box3 = {"product":"블랙커피", "money " :3500}

print(type(box)) #set
print(type(box2)) #list


box = list(box) # set -> list으로 변환
box2 = set(box2) # list->set으로 변환 
box3 = list(box3.values())
print(box)
print(box2)
print(box3)

