#python io

#파일 저장, 읽기 
import pickle as io

#w : 텍스트 저장 (write) 
#wb : 저장 + 바이너리..dump (이미지, 엑셀 등..)
#r : 텍스트 읽기(read)
#rb : 읽기(load) + 바이너리리


#-- w로 설정 시 write 사용 !문자전용 저장방식 
#pf = open("array.txt","w")
#data = "홍길덩님ㅋ"
#pf.write(data)



#-- wb로 설정 시 dump 사용 
#pf = open("array1.pickle","wb") #array1.pickle : .파일명 / 은 아무너가사용해도됨.
#data = [1,2,3,4,5]
#io.dump(data, pf) #dump는 wb, 바이너리 저장시 사용함

#pf.close()



rf = open("array1.pickle", "rb")  
result = io.load(rf)
print(result)

rf.close()


#print(pf) #<_io.BufferedWriter name='array.txt'> bufferstream과 비슷함 한번사용시 날라감
