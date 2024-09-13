# (過去のデータを元に翌日の気温を予測させる)

from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#csvの読み込み
df=pd.read_csv('weather_rog.csv',encoding='utf-8') 

#2013から2022のデータの学習用
training_year=(df['年'] <=2022)

#2023データ　テスト用
test_year=(df['年'] >=2023)

#予想させるために過去何日分のデータを使うか
interval=6

def make_data(data):
    #学習データ X
    x=[]
    #正解データ Y
    y=[]
    
    #気温の列をリスト化してtempsに入れる
    temps = list(data['気温'])
    
    #i=行番号
    for i in range(len(temps)):
        #例として2013.01.01より前のデータは存在しないから、interval0~5の時は次の処理
        #continue:条件に当てはまる場合、それ以降の処理は飛ばしてfor文の頭に戻る
        if i < interval : continue
        y.append(temps[i])
        xa = []
        #6日前〜前日までの6日分を、xaに貯めておく
        for p in range(interval):
            #例として2013.01.07だとすると、i=6,p=初期値だから0,interval=6
            #d=0
            d = i + p - interval
            #temps[0]は、2013.01.01の気温
            #xa[]に2013.1.1~1.6までの気温が入る
            xa.append(temps[d])
            #2013.1.1〜1.6の気温が、x=[]に追加される
        x.append(xa)
        
    return(x,y)

#帰ってきた関数をそれぞれの変数に入れる
training_x,training_y = make_data(df[training_year])

lr = LinearRegression()

#学習

lr.fit(training_x, training_y)

#学習終わりーーモデル完成ーー

#過去6日分の気温から明日の気温を予測
test_x = []

#平均気温の入力2024.6.14~20まで
#test_x.append([26.5,24.8,23.7,20.4,24.6,23.8])
#print('過去6日分の気温:',test_x)

#ターミナルからの入力
xa = []
for p in range(interval):
    print(str(interval-p) + '日前の気温を入力してください')
    xa.append(float(input()))
test_x.append(xa)

#プログラムの予想
pre_y = lr.predict(test_x)
print('明日の気温予想:',pre_y)




    
