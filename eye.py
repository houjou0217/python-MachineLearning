#顔は小さく目は大きく 雑コラ
import matplotlib.pyplot as plt
import cv2

#正面の顔にを認識するためのファイルを指定して読み込み
cascade_file = 'haarcascade_frontalface_alt.xml'
caccade = cv2.CascadeClassifier(cascade_file)

#グレースケールに変換する
img = cv2.imread('opencv/sample03.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#顔検出を実行
facelist = caccade.detectMultiScale(img_gray, minSize=(150,150))
if len(facelist) == 0:quit()

#顔と認識した部分を小さくする
for (x,y,w,h) in facelist:
    eye=cv2.resize(img[x:x+w,y:y+h],(int(w*0.9),int(h*0.9)))
    
    #その画像を雑コラ
    img[x:x+int(w*0.9),y:y+int(h*0.9)] = eye
    
#ここから目の処理
cascade_file = 'haarcascade_eye.xml'
caccade = cv2.CascadeClassifier(cascade_file)

#グレーススケールに変換
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#目の検出を実行する
eyelist = caccade.detectMultiScale(img_gray, minSize=(50,50))
if len(eyelist) == 0:quit()

#目と認識した部分を大きくする
for (x,y,w,h) in eyelist:
    eye=cv2.resize(img[x:x+w,y:y+h],(int(w*1.2),int(h*1.2)))
    
    #その画像を雑コラ
    img[x:x+int(w*1.2),y:y+int(h*1.2)] = eye
    
    #画像を出力する
    cv2.imwrite('opencv/eye.png',img)
    plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    plt.show()
    





    

