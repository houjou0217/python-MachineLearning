#画像の顔を認識させよう

import matplotlib.pyplot as plt 
import cv2

#xmlファイルを指定して読み込み　検出器を作成
cascade_file = 'haarcascade_frontalface_alt.xml'
caccade = cv2.CascadeClassifier(cascade_file)

#カラーは対応できないので、グレースケールに変換する
img = cv2.imread('opencv/sample01.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#顔検出の最小サイズ
facelist = caccade.detectMultiScale(img_gray, minSize=(50,50))

#検出できたかどうか
#顔が一つも検出できなかったら失敗と出力
if len(facelist) == 0:
    print("失敗")
    quit()
    

#顔と認識したところを赤い四角で囲む
for (x,y,w,h) in facelist:
    print('顔の座標=',x,y,w,h)
    #BGRよって（blue０、green0、red225となる）
    red = (0,0,225)
    
    #顔と認識した座標から、横の長さ、縦の長さ、色、線の太さ
    cv2.rectangle(img,(x,y),(x+w,y+h),red,thickness=10)

#画像を出力   
cv2.imwrite('opencv/sample01-red.png',img)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

    


