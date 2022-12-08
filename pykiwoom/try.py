import time
import datetime
from pykiwoom.kiwoom import *

# https://blog.naver.com/metania/222602334148


# 시간 측정 시작
start_time=time.time()

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

# ---------분봉 차트 조회-------------
# 900개 데이터가 한번에 전송됨.
tr="opt10080"
code="069500" #코덱스 200
set_d='20221109'

df_min = kiwoom.block_request(tr, 종목코드=code, 기준일자=set_d, 틱범위=1, output='주식분봉차트조회요청', next=0)

# 오늘 날짜 획득
dt_now = datetime.datetime.now()
# date='2022-12-09'
date=dt_now.strftime("%Y-%m-%d")

df_min=df_min[(df_min['체결시간'] >= pd.to_datetime(date+' 09:00:00')) & (df_min['체결시간'] <= pd.to_datetime(date + ' 10:00:00'))]

df_min=df_min.sort_values(by='체결시간')

print(df_min.info())

df_min.to_csv('분봉데이터.csv')

end_time=time.time()
elapsed_time=end_time-start_time