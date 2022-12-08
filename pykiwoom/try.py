import time
import datetime
from pykiwoom.kiwoom import *

# 1.
# https://blog.naver.com/metania/222602334148

# 2.
# https://trustyou.tistory.com/351

# 3.
# https://netpilgrim.net/1059

# 4.
# https://programmingfbf7290.tistory.com/entry/4-%EC%A3%BC%EC%8B%9D-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%B6%88%EB%9F%AC%EC%98%A4%EA%B8%B0-%ED%82%A4%EC%9B%80-open-api-%EC%A3%BC%EC%8B%9D-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%ED%85%8C%EC%8A%A4%ED%8A%B8-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D

#5.
# https://velog.io/@dingger/%ED%82%A4%EC%9B%80-API-%EC%82%AC%EC%9A%A9-%EC%B2%AB%EA%B1%B8%EC%9D%8C


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