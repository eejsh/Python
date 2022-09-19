#문자열 자르기 및 해당 문자열 가져오기 (배열 구조 이므로 무조건 0부터 시작함)
gender ="911101-2345678"
print("성별 :" +  gender[7])  # 배열로 8번재 값을 가져옴
print("월일 :" + gender[2:6]) # 6번째 직전까지 문자를 가져옴 문자열(2~5까지)
print("생년월일 : " + gender[:6]) # 무조건 0부터 시작하여 문자열을 가져옴
print("주민번호 뒷자리 : " + gender[7:]) # 해당 문자열 부터 끝까지 출력

print("생년월일 : " + gender[:-8]) # -1부터는 문자열 거꾸로 넘버링을 하게 됩니다.


word = "Python Programing"
print(word.lower()) # lower : 전체를 소문자
print(word.upper()) # upper : 전체를 대문자
print(word[2].islower()) # is는 문자열에 대한 검토를 할 때 사용하는 문법, islower, isupper  (ischecked와 비슷)
print(len(word)) # 문자 갯수 len (length) 뜻 , length 사용 시 오류..
print(word.replace("Python", "java")) #  replace 는 단어를 변경 할 때 = (출력 :java Programing)
print(word.index("g")) # 해당 문자열에 대한 문자위치 번호를 출력함 (g단어 찾아 위치 출력)
print(word.index("P"))
i = word.index("P") # 문자열에서 동일한 단어가 있어도 첫번째 찾는 단어에 대한 번호출력 (10)
i = word.index("P", i + 1) # 문자열에 동일한 단어 다음것을 찾아서 출력하는 번호 (0)
print(i) #7

#find -1 : 문자열 또는 단어가 없을 경우
print(word.find("gral")) #find 문자열을 찾을 때 사용합니다. (indexOf)와 동일한기능
print(word.count("P")) #동일한 문자 갯수가 몇개 인지를 카운팅 하는 문법
