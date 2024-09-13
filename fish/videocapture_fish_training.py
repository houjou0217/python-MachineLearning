# 魚を学習させる

# glob : 条件を満たすパスを見つける
import cv2, os, pickle, glob
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# pythonでファイルのパスを取得
path = os.path.dirname(os.path.abspath(__file__))
path_fish = path + '/yesfish'
path_nofish = path + '/nofish'

# 画像の学習サイズ
img_size = (64,32)

# 学習データを格納するリスト
x = []

#　教師用のデータを格納するリスト（ラベルデータ）
y = []

# 画像データを読み込んで、配列に追加する関数
def read_def(path, label):
    files = glob.glob(path + '/*.jpeg')
    for f in files:
        img = cv2.imread(f)
        print(f)
        img = cv2.resize(img, img_size)
        img_data = img.reshape(-1,)
        x.append(img_data)
        y.append(label)
        
# 画像データを読み込む
read_def(path_nofish, 0)
read_def(path_fish, 1)

# データを学習用とテスト用に分割
x_training, x_test, y_training, y_test = \
    train_test_split(x,y,test_size=0.2)

# データを学習
clf = RandomForestClassifier()
clf.fit(x_training, y_training)

# 精度の確認
y_pred = clf.predict(x_test)
print(accuracy_score(y_test, y_pred))

# 学習モデルを保存
with open('fish.pkl', 'wb') as fp:
    pickle.dump(clf, fp)


