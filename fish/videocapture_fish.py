#動画から魚を抽出してみよう！
#方法：動画内で動きのある部分のキャプチャを撮る

#osモジュールとはosに依存する機能を利用する(今回はディレクトリ操作.フォルダ操作..大量の写真を使いたいため)
import cv2, os



#前の画像を格納
img_before = None
#画像の枚数をカウント
no = 0
#保存するディレクトリ名
save_dif = 'fishPhoto'
#ディレクトの作成
#os.mkdir(save_dif)


#動画ファイルを指定
cap = cv2.VideoCapture('fish/fish.mp4')
while True:
    #is_ok:フラグ（true.false）frame:画像
    #画像の取得
    is_ok, frame = cap.read()
    if not is_ok : break
    #is_okがtrueだったら
    frame = cv2.resize(frame, (640,360))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #gaussianBlurはぼかしをかける　邪魔なチリやゴミを除去するため（ノイズ除去）
    gray = cv2.GaussianBlur(gray, (15,15), 0)
    #画像を２値化する（白か黒かに分けるgrayは存在しない状態）
    img_now = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)[1]
    
    if not img_before is None:
        #画像の差分
        frame_dif = cv2.absdiff(img_before, img_now)
        #輪郭の抽出
        count = cv2.findContours(frame_dif,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
        for pt in count:
            #差分があったら
            x,y,w,h = cv2.boundingRect(pt)
            if w < 100 or w > 500: continue
            #抽出した領域を画像として保存
            img = frame[y:y+h, x:x+w]
            outfile = save_dif + '/' + str(no) + '.jpeg'
            cv2.imwrite(outfile, img)
            no += 1

    img_before = img_now

cap.release()
print('ok')