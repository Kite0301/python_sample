from menu import Menu

class Food(Menu):
    def __init__(self, name, price, calorie):
        super().__init__(name, price)
        self.calorie = calorie


    def info(self):
        return str(self.calorie) + 'kcal、' + str(self.price) + '円の' + self.name


    def calorie_info(self):
        return self.name + 'は' + str(self.calorie) + 'kcalです'
