import talib
import numpy as np
import pandas as pd

class InputBuilder():

    def make_basic_features(self, df: pd.DataFrame):
        ma = talib.MA(df['close'], timeperiod=30)
        macd, macdsignal, macdhist = talib.MACD(df['close'])
        rsi = talib.RSI(df['close'], timeperiod=14)
        ad = talib.AD(df['high'], df['low'], df['close'], df['volume'])

        df['ma'] = ma
        df['macd'] = macd
        df['macdsignal'] = macdsignal
        df['macdhist'] = macdhist
        df['rsi'] = rsi
        df['ad'] = ad

    def make_window_features(self, df: pd.DataFrame, cols=['ma', 'macd', 'macdsignal', 'macdhist', 'rsi', 'ad'], window_size=10):
        for col in cols:
            prev_summary = df[col].rolling(window=window_size).mean().shift(1)
            df[f'{col}_w'] = (df[col] - prev_summary)
    
    def make_target(self, df: pd.DataFrame, threshold=1000000000):
        sub_tv = [0 for i in range(len(df))]
        for i in range(1,len(df)):
            sub_tv[i] = df['trade_volume'][i]-df['trade_volume'][i-1]
        df['label'] = 'H'
        ishold = False
        for i in range(len(df)):
            if (ishold == False) and (sub_tv[i]>threshold):
                df['label'][i+1] = 'B'
                ishold = True
            elif (ishold == True) and (sub_tv[i]<-threshold):
                df['label'][i+1] = 'S'
                ishold = False
            else:
                pass

df = pd.read_csv('collectKODEX200.csv').drop('Unnamed: 0', axis=1)
ib = InputBuilder()
ib.make_basic_features(df)
ib.make_window_features(df)
ib.make_target(df)
df.to_csv('KODEX200.csv')
