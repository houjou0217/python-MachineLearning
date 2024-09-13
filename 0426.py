A=4
A=A/2
print(A)


txt='北條'
txt1='慎乃輔'

print(txt + txt1)

len(txt)

todo=["プレゼン資料","昼食","会議","メール対応"]
print(todo[2])

todo.append("定時退社")
print(todo)



print(todo[1:4])

todo.remove('メール対応')
print(todo)

#joinを使ってリストを結合して表示
print('→'.join(todo))

#splitを使って区切る
"""str='→'.join(todo)
print(str.split('→'))

#inputで受け取る
name=input()
print("こんにちは、"+name+"さん！")

#受け取った数字の足し算
num1=input()
num2=input()
print(int(num1)+int(num2))"""

# if文を使ったじゃんけん
"""import random
hand=int(input())
hand1=random.randint(0,2)
if hand==0 and hand1==1:
    print("WINEER hand")
elif hand==0 and hand1==2:
    print("WINEERhand1")
elif hand==1 and hand1==0:
    print("WINNERhand1")
elif hand==1 and hand1==2:
    print("WINNERhand")
elif hand==2 and hand1==0:
    print("WINNERhand")
elif hand==2 and hand1==1:
    print("WINNERhand1")
else:
    print("drow")"""
    
#for文とリスト
price=[100,120,150]
for i in price:
    num=i*0.7
    print(int(num))
    

    
