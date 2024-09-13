import matplotlib.pyplot as plt
import cv2

#自分で描いたmosaic関数を呼び出す
from mosaic_def import mosaic as mosaic

#画像の読み込み
img = cv2.imread('opencv/mosaicTest.png')
#モザイク処理 mosaic関数で書いた引数に当てはめる
#画像を格納した引数、範囲(x,y,横幅,縦幅),モザイクのピクセル数
mos = mosaic(img,(50,50,500,500),15)

#モザイクをかけた画像の出力
cv2.imwrite('opencv/mosaic-test01.png', mos)
plt.imshow(cv2.cvtColor(mos, cv2.COLOR_BGR2RGB))
plt.show()