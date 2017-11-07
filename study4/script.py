class Menu(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        return self.name + ' ' +  str(self.price) + '円'

    def get_total_price(self, count):
        total_price = self.price * count
        if count >= 3:
            total_price -= 100
        return total_price

menu1 = Menu('ピザ', 800)
menu2 = Menu('すし', 1000)
menu3 = Menu('コーラ', 300)
menu4 = Menu('お茶', 200)

menus = [menu1, menu2, menu3, menu4]

index = 0
for menu in menus:
    print(str(index) + '. ' + menu.info())
    index += 1

print('--------------')
order = int(input('メニューの番号を選択してください: '))

selected_menu = menus[order]
print('選択されたメニュー: ' + selected_menu.name)

count = int(input('個数を入力してください(3つ以上で100円割引): '))
print('お会計は' + str(selected_menu.get_total_price(count)) + '円です')
