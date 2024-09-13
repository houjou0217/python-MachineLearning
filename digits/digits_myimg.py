#手書き数字を判別しよう
import cv2
import pickle

def predict_digits(filename):
    with open('digits/digits.pkl','rb') as fp:
        clf = pickle.load(fp)
        
        #用意した手書きの画像ファイルを読み込む
        my_img=cv2.imread(filename)
        #画像データを学習済みデータに合わせる
        
        #1. グレースケールに変換する
        my_img=cv2.cvtColor(my_img, cv2.COLOR_BGR2GRAY)
        
        #2. 8*8サイズに変換する
        my_img=cv2.resize(my_img,(8,8))
        
        #3.白黒を反転させる
        #16~0に置き換えたいので16で割る　//で切り捨てることができる
        my_img=15 - my_img // 16
        
        #4.二次元を一次元に変換する
        my_img=my_img.reshape((-1,64))
        
        #予測
        res = clf.predict(my_img)
        return res[0]
    
        #画像ファイルを指定して実行
n = predict_digits('digits/my2.png')
print('私の書いた'+str(n))