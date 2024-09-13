#手書き数字を判別しよう

import matplotlib.pyplot as plt

#scikitlearnに標準搭載されている手書き数字のデータセットの読み込み

from sklearn import datasets
digits = datasets.load_digits()

"""#搭載されているデータの一部を出力する　試しに15個出力す
for i in range(15):
    #subpot(行数、列数、何番目に出力するか)
    plt.subplot(3,5,i+1)
    #軸表示
    plt.axis('off')
    #タイトルを表示
    plt.title(str(digits.target[i]))
    #グレースケールで表示する
    plt.imshow(digits.images[i], cmap='gray')
    
plt.show()"""

#一文字を詳しく調べる
#数字データは8*8ピクセルで、0〜16の明暗で表している0に近いほど黒い16に近いほど白い

digits_up=digits.images[1]
plt.imshow(digits_up, cmap='gray')
print(digits_up)
plt.show()


