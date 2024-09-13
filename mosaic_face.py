import matplotlib.pyplot as plt
import cv2
from mosaic_def import mosaic as mosaic

cascade_file = 'haarcascade_frontalface_alt.xml'
caccade = cv2.CascadeClassifier(cascade_file)

#カラーは対応できないので、グレースケールに変換する
img = cv2.imread('opencv/sample01.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

facelist = caccade.detectMultiScale(img_gray, minSize=(50,50))
if len(facelist) == 0:quit()

#顔と認識した部分にモザイク処理をする
for (x,y,w,h) in facelist:
    img = mosaic(img, (x,y,x+w,y+h),10)

#画像を出力    
cv2.imwrite('opencv/sample01_mosaic.png', img)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()