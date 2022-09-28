#산점도 응용 부분

import pandas as pd
import matplotlib.pyplot as mpt
import mfont



#scatter : x축, y축
data = pd.read_csv("movie.csv", encoding="euc-kr")
#c : color + cmap(자동색상)


#scatter 에서 text 사용 시 x축, y축에 대한 값이 모두 int로 이루어져 있어야 반복문으로 적용 할 수 있습니다. 
mpt.scatter(data['지역'], data['관객수'], sizes=data['관객수']+100, c=data['관객수'])
mpt.colorbar()
mpt.xlabel("지역")
mpt.ylabel("관객수")
mpt.show()