#10年分の名古屋の平均気温を学習したモデルを作る
#過去一週間の気温を入れて、明日の気温を予測させる

datafile='weather_data.csv'
outfile='wether_rog.csv'

#csv ファイルを一行ずつ読み込み
#withをつけておくとインデントのついている行の処理が終わったら自動的にファイルを閉じる
with open(datafile,'rt',encoding='shift-jis') as fr:
    lines=fr.readlines()
    
#いらないヘッダーを消して、新いヘッダーを設定する
lines=['年,月,日,気温,品質,均質/n'] + lines[5:]

lines=map(lambda v: v.replace('/',','), lines)  
#listであるlinesを文字列に変換する
result=''.join(lines).strip()
print(result)

#結果をファイルに出力
with open(outfile,'wt', encoding='utf-8') as fw:
    fw.write(result)
    print("ok")

#csvデータの変換