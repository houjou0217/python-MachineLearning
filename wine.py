import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

#csvデータ読み込み
wine=pd.read_csv('winequality.csv',sep=',',encoding='utf-8')
print(wine)

#データトラベルに分ける
#xは学習データquality列を消したもの/yは正解データquality列のみ抽出したもの
x=wine.drop('quality',axis=1)
y=wine['quality']

#データに対して三分割する　低中高品質とラベルで付け直す
newlist=[]
for i in list(y):
    if i <=4:
        newlist +=[0]
    elif i <=7:
        newlist+=[1]
    else:
        newlist+=[2]

y=newlist
    
#各データを学習用とテスト用に分割
x_training,x_test,y_training,y_test = train_test_split(x,y,test_size=0.2)

#学習させる
clf = RandomForestClassifier()
#前が学習データ　後ろが正解データ
clf.fit(x_training,y_training)

#--学習モデルが完成--

ans = clf.predict(x_test)
#前が正解データ　後ろがAIが予測してきたデータ
print(classification_report(y_test, ans))
#y_testは人間のソムリエが判断したデータ
print("正解率:",accuracy_score(y_test, ans))

#--今の状態だと正解率が7割くらいになるの--

import matplotlib as plt

count_data=wine.groupby('quality')['quality'].count()
print(count_data)

#データをグラフに表す
count_data.plot()
plt.savefig('wine-plt.png')
plt.show()

#クオリティの567が多くて、ないものもある
#不均衡データ

