class Menu:
    def __init__(self, name, price):
        self.name = name
        self.price = price


    def info(self):
        return str(self.price) + '円の' + self.name


    def get_total_price(self, count):
        total_price = self.price * count
        if count >= 3:
            total_price -= 100
        return total_price
