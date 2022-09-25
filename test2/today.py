from datetime import *
#오늘 날짜 및 시간 출력


#오늘날짜
today = datetime.now().replace(microsecond=0)
print(today)


#현재시간
day = today.date()
print(day)


time = today.time()
print(time)


print(time.replace(microsecond=0)) # 초 부분에 소수점을 없앰



#시간을 문자열로 변환 => DB 저장시 필요

time = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
print(time)