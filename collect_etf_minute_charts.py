from pykiwoom.kiwoom import *
import time
import pandas as pd

tr_dic = {'069500':'kodex_200', '114800':'kodex_inverse'}

def makedf(code):
    kiwoom.SetInputValue("종목코드", code)
    kiwoom.SetInputValue("틱범위", "1")
    kiwoom.CommRqData("opt10080", "opt10080", "0", "0101")



if __name__ == "__main__":
    # 로그인
    kiwoom = Kiwoom()
    kiwoom.CommConnect(block=True)

    for code, name in tr_dic.items():
        print(code, name)
        makedf(code)