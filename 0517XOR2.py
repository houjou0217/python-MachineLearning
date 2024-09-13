from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

#学習データと正解データ
learn_data=[[0,0],[1,0],[0,1],[1,1]]
learn_label=[0,1,1,0]

#LinerSVCをインスタンス化
clf=KNeighborsClassifier(n_neighbors= 1)

clf.fit(learn_data,learn_label)

#-----------学習データはここまで-------------

#test
test_data=[[1,1],[0,1],[1,0],[0,0]]
#予測を返す関数
test_label=clf.predict(test_data)
#結果出力
print(test_data,"予測結果",test_label)
#正解率
print(accuracy_score([0,1,1,0],test_label))

#n_neighborsのパラメーター、自分から一番近い学習データの数
#Ex n_nerighbors=1の時0,0が入ってきたら
#学習データの中から、テストデータに一番近い１個を探す
