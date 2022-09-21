from bs4 import BeautifulSoup
from requests import *

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
