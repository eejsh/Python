from bs4 import BeautifulSoup
from requests import *
#해당 사이트에 접속하여 Devtool로 볼 경우 data가 확인이 되지만 실제 크롤링 후 스크래핑 시 데이터가 확인이 안될 경우는
#ajax 및 자바스크립트로 직접 태그가 생성 되도록 제작한 되었음. 이럴경우 스크래핑 하기가 어려워짐. 

url = "https://www.koreabaseball.com/TeamRank/TeamRank.aspx"
result = get(url)
print(result.raise_for_status()) #none

html = BeautifulSoup(result.text, "lxml")
baseball = html.find("div", attrs={"id":"cphContents_cphContents_cphContents_udpRecord"})
team = baseball.find("tbody")
tr = team.find_all("tr")

#td = tr[1].find_all("td") #반복문 아에들어가야됨 (팀명)


w=0
for a in tr:
     td = tr[w].find_all("td")
     print(td[1])
     w+=1


#print(team)
#print(tr)
#print(td)

print(td[0])


#ajax로 구성된 html은 한번 크롤링해야 편함..
