from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)
print("블록킹 로그인 완료")


last200 = kiwoom.GetMasterLastPrice('069500')
lastInverse = kiwoom.GetMasterLastPrice('226490')

print(last200)
print(lastInverse)

# 조건식을 pc로 다운로드
kiwoom.GetConditionLoad()

# 전체 조건식 리스트 얻기exi
conditions = kiwoom.GetConditionNameList()

# 0번 조건식에 해당하는 종목 리스트 출력
condition_index = conditions[0][0]
condition_name = conditions[0][1]
codes = kiwoom.SendCondition("0101", condition_name, condition_index, 0)

print(codes)

# ---------매수---------

# 주식계좌
accounts = kiwoom.GetLoginInfo("ACCNO")
stock_account = accounts[0]

# 삼성전자, 10주, 시장가주문 매수
kiwoom.SendOrder("시장가매수", "0101", stock_account, 1, "005930", 10, 0, "03", "")

# ---------매도---------
kiwoom.SendOrder("시장가매도", "0101", stock_account, 2, "005930", 10, 0, "03", "")

# 분봉 데이터 조회
import pandas

date = '20221111'
etf = kiwoom.GetCodeListByMarket('8')
df = kiwoom.block_request('opt20005', #trcode 업종분봉조회요청	
                          종목코드=etf,
                          output="주식분봉차트조회",
                          기준일자=date,
                          수정주가구분=1,
                          next=0)
df.to_csv('data.csv')
