#openCVを使って画像処理をしてみる
import matplotlib.pyplot as plt
import cv2

#画像の読み込み
img = cv2.imread('opencv/sample01.jpg')
#plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#plt.show()

#画像の保存（例えば拡張子を変える）
#cv2.imwrite('opencv/output.png', img)

#画像サイズを変える 横幅、縦幅
img_resize = cv2.resize(img,(500,700))
cv2.imwrite('opencv/sample01-resize.png', img_resize)

#画像のトリミング
#開始座標Y:終了座標Y,開始座標X:終了座標X
img_trim = img[40:240,410:600]
cv2.imwrite('opencv/sample01-trim.jpg', img_trim)


