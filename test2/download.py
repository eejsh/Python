from urllib import* 
from requests import *

#urllib 다운로드 기능

def download(url):
     with open("tmon.html", "wb") as file:
          response = get(url)
          file.write(response.content)

url =  "http://search.tmon.co.kr/search/?keyword=%EA%B2%BD%EA%B8%B0%ED%8E%9C%EC%85%98"

download(url);
