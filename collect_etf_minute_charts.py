from pykiwoom.kiwoom import *
import time
import pandas as pd
import pickle
from tqdm.auto import tqdm

tr_dic = {
  'opt20005': {'001': 'kospi', '201': 'kospi200'},
  'opt10080': {'069500':'kodex_200', '114800':'kodex_inverse', '226490':'kodex_kospi'}
}

def make_argument_dic(tr_code, code, is_next=False):
                      # tr code, 종목 코드명, 다음에 더 있는지
    arg_dic = {'틱범위': "1", 'next':2 if is_next else 0}   # 틱범위는 통상적으로 1로 설정
    if tr_code == 'opt10080':   # 주식분봉차트
        arg_dic.update({'종목코드': code, 'output': "주식분봉차트조회", '수정주가구분': "1"})
    elif tr_code == 'opt20005': # 업종분봉차트
        arg_dic.update({'업종코드': code, 'output': "업종분봉조회"})
    else:
        assert False, "Unknown tr_code"
    return arg_dic

if __name__ == "__main__":
    kiwoom = Kiwoom() # 키움 인스턴스 생성
    kiwoom.CommConnect(block=True) # 로그인

    for tr_code, dic in tr_dic.items():
        for code, name in dic.items():
            df = kiwoom.block_request()

# 흠... 어케해야하지?