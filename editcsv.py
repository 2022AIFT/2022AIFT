import pandas as pd
df = pd.read_csv('collectKODEX200.csv').drop('Unnamed: 0', axis=1) # 첫번째 열 제거
df = df.sort_values('date').reset_index(drop=True) # 날짜 오름차순 정렬

df['sub_tv']=0
for i in range(1, 96966):
  df['sub_tv'][i] = df['trade_volume'][i]-df['trade_volume'][i-1]

df['label'] = 'H'
ishold = False # 초기 상태 False
newdf = df.copy() # df 참조 오류때문에 copy함
for i in range(1, 96966):
  # 보유중이지 않고, 10억보다 크면
  if (ishold == False) and (newdf['sub_tv'][i]>1000000000):
    newdf['label'][i+1] = 'B' # 다음 분봉에 매수
    ishold = True # 보유 중으로 변경
  # 보유중이고, -10억보다 작으면
  elif (ishold == True) and (newdf['sub_tv'][i]<-1000000000):
    newdf['label'][i+1] = 'S' # 다음 분봉에 매도
    ishold = False
  # 보유하고 있지 않거나, -10억<sub_tv<10억인 경우
  else:
    pass # H(아무것도 하지 않음)

openprice = 0 # 초기값 0
result = [] # 수익 리스트
for i in range(96966):
  if newdf['label'][i] == 'B':
    openprice = newdf['open'][i] # B로 레이블되었을 때 현재가
  elif newdf['label'][i] == 'S':
    result.append(newdf['open'][i] - openprice)
  else:
    pass

print(sum(result)) # 해당 전략으로 매수/매도시 1주당 926585의 수익을 얻을 수 있음

newdf.to_csv('NewKODEX200.csv') # csv 파일 저장