#手書きを判別しよう2

from sklearn.model_selection import train_test_split
from sklearn import datasets, svm
from sklearn.metrics import accuracy_score

#データセット読み込み
digits = datasets.load_digits()

#数字の二次元リスト
x=digits.images
#数字のタイトル
y=digits.target

#reshape():リスト内の形状を変える、次元を変える8*8のリストを1*64に変える
#今回学習で使うアルゴリズムでは（SVC)では一次元リストしか使えないから
x = x.reshape((-1,64))

#学習用とテスト用に分割する
x_training, x_test, y_training ,y_test = train_test_split(x,y,test_size=0.2)

#学習
clf=svm.SVC()
clf.fit(x_training, y_training)

#予測させて精度を確認
y_pred=clf.predict(x_test)
print(accuracy_score(y_test, y_pred))

#学習済みモデルを保存
#pickle というもジェールを使う
import pickle 
with open('digits.pkl','wb') as fp:
    pickle.dump(clf, fp)
    

