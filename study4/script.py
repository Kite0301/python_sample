from menu import Menu

menu1 = Menu('サンドイッチ', 500)
menu2 = Menu('チョコケーキ', 400)
menu3 = Menu('コーヒー', 300)
menu4 = Menu('オレンジジュース', 200)

menus = [menu1, menu2, menu3, menu4]

index = 0

for menu in menus:
    print(str(index) + ': ' + menu.info())
    index += 1

print('--------------')

order = int(input('メニューの番号を入力してください: '))
selected_menu = menus[order]
print('選択されたメニュー: ' + selected_menu.name)

count = int(input('個数を入力してください(3つ以上で1割引): '))
result = selected_menu.get_total_price(count)
print('合計は' + str(result) + '円です')
