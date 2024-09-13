#画像の一部をモザイクにする関数
import cv2

def mosaic(img, rect, size):
    #モザイク処理をかける領域
    (x1,y1,x2,y2) = rect
    w = x2 - x1
    h = y2 - y1
    i_rect = img[y1:y2, x1:x2]
    #モザイク加工にするため、一度縮小して拡大する（わざと粗くする）
    
    i_small = cv2.resize(i_rect,(size,size))
    i_mos = cv2.resize(i_small,(w,h),interpolation=cv2.INTER_AREA)
    #元の画像にモザイク処理をした部分を重ねる
    img2 = img.copy()
    img2[y1:y2, x1:x2] = i_mos
    return img2

    