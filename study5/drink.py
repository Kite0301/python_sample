from menu import Menu

class Drink(Menu):
    def __init__(self, name, price, amount):
        super().__init__(name, price)
        self.amount = amount


    def info(self):
        return str(self.amount) + 'mL、' + str(self.price) + '円の' + self.name
