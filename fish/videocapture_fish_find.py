# 実際に動画から抽出しよう

import cv2, os, pickle, copy

with open('fish.pkl', 'rb') as fp:
    clf = pickle.load(fp)
    
# ベストショット画像を保存するディレクトリを設定
output_dir = './bestshot'

#前の画像を格納
img_before = None

# ベストショットに出力するしきいち
fish_th = 3
count = 0
frame_count = 0

# ベストショットディレクトリの作成
if not os.path.isdir(output_dir):
    os.mkdir(output_dir)

# 動画ファイルから入力開始
cap = cv2.VideoCapture('fish.mp4')
while True:
    
    is_ok, frame = cap.read()
    if not is_ok : break
    #is_okがtrueだったら
    frame = cv2.resize(frame, (640,360))
    frame2 = copy.copy(frame)
    frame_count += 1
    
    # 前のフレームと比較するために画像を変更
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (15,15), 0)
    img_now = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)[1]
    if not img_before is None:
        #画像の差分
        frame_dif = cv2.absdiff(img_before, img_now)
        count = cv2.findContours(frame_dif,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
        
    