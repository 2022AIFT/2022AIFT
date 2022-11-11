from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)
print("블록킹 로그인 완료")


last200 = kiwoom.GetMasterLastPrice('069500')
lastInverse = kiwoom.GetMasterLastPrice('226490')

print(last200)
print(lastInverse)