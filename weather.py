import pandas as pd

#pandasでCSVデータを読み込む
df=pd.read_csv('weather_rog.csv',encoding='utf-8') 

#日付ごとに気温をリストにまとめる
#辞書
md={}

#iterrows 1行ずつ取得
#i=添字　row=1行分のデータが表形式で格納される
for i , row in df .iterrows():
    m,d,v = (int(row['月']), int(row['日']), float(row['気温']))
    #format関数でmに１個目の月を入れる、dに１個目の日を入れる
    #01/01の表記にするため
    
    key='{:02d}/{:02d}'.format(m,d)
    if not(key in md):
        #もしもキーがなかったらカラのリストを作る
        md[key]=[]
    md[key] += [v]
    
#日付ごとに平均を求める
avs={}
for key in sorted(md):
    avs[key] = sum(md[key]) / len(md[key])
    print('{0}:{1}'.format(key,avs[key]))   
    
#月ごとの平均気温をまとめて描画してみる
import matplotlib.pyplot as plt
#月単位でのグルーピング
"""  g=df.groupby(['月'])['気温']
gg= g.sum() / g.count()
print(gg) 
gg.plot()
plt.savefig('kion.png')
plt.show()

gg.plot()
#plt.saving('kion.png')  
#plt.show()  """

#年ごとで平均気温が30度を超えた日をカウントする
hot_bool = (df['気温'] > 30)
hot=df[hot_bool]

#年ごとにカウント
cnt=hot.groupby(['年'])['年'].count()
print(cnt)

#描画
cnt.plot()
plt.savefig('kion30over.png')
plt.show()

#いろんなグルーピングの例を作った