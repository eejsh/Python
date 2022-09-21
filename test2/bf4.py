from bs4 import BeautifulSoup
from requests import *

url = "https://www.nate.com"
res = get(url)
res.raise_for_status()

result = BeautifulSoup(res.text, "lxml") 
#태그 이름을 적용하여 태그안에 있는 text를 가져올 수 있음.
#단, 중복된 태그가 있을 경우 제일 먼저 읽어오는 라인만 처리가 됨. (ex:title이 두개가 있으면 처음타이틀만 읽음)

#print(result.title)
#print(result.title.get)
#print(result.title.get_text())

#find : 해당 단어를 찾습니다. attrs (attribute의 약자(속성값)) : class 속성 중 iskeyword만 가져오기.)
rank = result.find("div", attrs={"class" : "isKeyword"})


#print(len(rank.li)) #반복되는 태그의 갯수를 확인 함 (nate의 iskeyword = 5개..)

#print(rank.h4.get_text()) #실시간 이슈 키워드
#print(rank.li)


#find는 1개, find_all 해당 부모 마크업 안에 있는 모든 태그를 말함.

#rank에만 속하는 태그 중 span 이라는 태그와 해당 클래스명 검토 (find) 
ranknum = rank.find_all("span", attrs={"class":"num_rank"}) 

#find_all : 기본으로 배열로 구조가 변경됩니다. 

#print(ranknum.get_text())

ranksubject = rank.find_all("span", attrs={"class":"txt_rank"})
#print(ranksubject.get_text())


w=0
for bb in ranknum:
     print(bb.get_text())
     print(ranksubject[w].get_text())
     w+=1

for cc in ranksubject:
     print(cc.get_text())