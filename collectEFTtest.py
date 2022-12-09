import sys
from PyQt5.QAxContainer import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import time
import pandas


class minute_data():

    def __init__(self):
        self.ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        print("연결 완료")

        self.ocx.dynamicCall("CommConnect()")
        self.login_event_loop = QEventLoop()
        self.ocx.OnEventConnect.connect(self.OnEventConnect) # 로그인
        self.login_event_loop.exec_() # OneventConnect 함수에서 self.login_event_loop.exit() 실행되면 exec 실행

        
        self.ocx.OnReceiveTrData.connect(self.OnReceiveTrData) # TR 데이터 받음

        
        

    def rq_mindata(self, itemcode, tic, justify):
        self.min_data = {'date':[], 'open':[], 'high':[], 'low':[], 'close':[], 'volume':[], 'trade_volume':[]}

        self.ocx.dynamicCall("SetInputValue(Qstring, Qstring)", "종목코드", itemcode)
        self.ocx.dynamicCall("SetInputValue(Qstring, Qstring)", "틱범위", tic)
        self.ocx.dynamicCall("SetInputValue(Qstring, Qstring)", "수정주가구분", justify)
        # CommRqData(rqname, trcode, next,screen)
        self.ocx.dynamicCall("CommRqData(Qstring, Qstring, int, Qstring)", "rqname_opt10080", "opt10080", 0, "0101")
        self.tr_event_loop = QEventLoop()
        self.tr_event_loop.exec_()

        while self.remained_data == True:
            self.ocx.dynamicCall("SetInputValue(Qstring, Qstring)", "종목코드", itemcode)
            self.ocx.dynamicCall("SetInputValue(Qstring, Qstring)", "틱범위", tic)
            self.ocx.dynamicCall("SetInputValue(Qstring, Qstring)", "수정주가구분", justify)
            # CommRqData(rqname, trcode, next,screen)
            self.ocx.dynamicCall("CommRqData(Qstring, Qstring, int, Qstring)", "rqname_opt10080", "opt10080", 2, "0101")
            self.tr_event_loop = QEventLoop()
            self.tr_event_loop.exec_()

    def OnEventConnect(self, erro_code):
        if erro_code == 0:
            print("로그인 성공")
        else:
            print("로그인 실패")
        self.login_event_loop.exit()
        print("로그인 루프 종료")

    def GetCommData(self, trcode, recordname, index, itemname):
        result = self.ocx.dynamicCall("GetCommData(Qstring, Qstring, int, Qstring)", trcode, recordname, index, itemname)
        return result

    def opt10080(self, trcode, recordname):
        getrepeatcnt = self.ocx.dynamicCall("GetRepeatCnt(Qstring, Qstring)", trcode, recordname)
        for i in range(getrepeatcnt):
            item_code = self.GetCommData(trcode, recordname, 0, "종목코드").strip()
            close = self.GetCommData(trcode, recordname, i, "현재가").strip()
            volume = self.GetCommData(trcode, recordname, i, "거래량").strip()
            date = self.GetCommData(trcode, recordname, i, "체결시간").strip()
            open = self.GetCommData(trcode, recordname, i, "시가").strip()
            high = self.GetCommData(trcode, recordname, i, "고가").strip()
            low = self.GetCommData(trcode, recordname, i, "저가").strip()
            trade_volume = int(volume)*int(close) # 거래대금

            self.min_data['date'].append(date)
            self.min_data['open'].append(open)
            self.min_data['high'].append(high)
            self.min_data['low'].append(low)
            self.min_data['close'].append(close)
            self.min_data['volume'].append(volume)
            self.min_data['trade_volume'].append(trade_volume)

    def OnReceiveTrData(self, scrno, rqname, trcode, recordname, prenext):
        if prenext == '2':
            self.remained_data = True
        elif prenext != '2':
            self.remained_data = False

        if rqname == 'rqname_opt10080':
            self.opt10080(trcode, recordname)
        try:
            self.tr_event_loop.exit() # 여기서 무한 루프
        except AttributeError:
            pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    min = minute_data()
    min.rq_mindata("069500", 1, 1)
    df_min_data = pandas.DataFrame(min.min_data, columns=['date', 'open', 'high', 'low', 'close', 'volume', 'trade_volume'])
    print(df_min_data)