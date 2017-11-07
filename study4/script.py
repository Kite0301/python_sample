from menu import Menu

menu1 = Menu('ピザ', 800)
menu2 = Menu('すし', 1000)
menu3 = Menu('コーラ', 300)
menu4 = Menu('お茶', 200)

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
print('金額は' + str(selected_menu.get_total_price(count)) + '円です')
