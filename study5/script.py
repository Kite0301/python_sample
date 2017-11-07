from food import Food
from drink import Drink

food1 = Food('ハンバーガー', 500, 300)
food2 = Food('チーズバーガー', 600, 350)
food3 = Food('ホットッドッグ', 300, 250)

foods = [food1, food2, food3]

drink1 = Drink('コーラ', 200, 400)
drink2 = Drink('ホットコーヒー', 300, 250)
drink3 = Drink('天然水', 100, 400)

drinks = [drink1, drink2, drink3]

print('食べ物メニュー')
index = 0
for food in foods:
    print(str(index) + ': ' + food.info())
    index += 1

print('飲み物メニュー')
index = 0
for drink in drinks:
    print(str(index) + ': ' + drink.info())
    index += 1

print('--------------')
order = int(input('食べ物の番号を選択してください: '))
selected_food = foods[order]

order = int(input('飲み物の番号を選択してください: '))
selected_drink = drinks[order]

count = int(input('何セット買いますか？(3つ以上で1割引): '))
total_price = selected_food.get_total_price(count) + selected_drink.get_total_price(count)
print('金額は' + str(total_price) + '円です')
