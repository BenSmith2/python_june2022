class Product():
    def __init__(self, name, price, category, available_at):
        self.name = name
        self.price = price
        self.category = category
        self.available_at = available_at
        self.available_at.add_products(self.name, self.price)

    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price += self.price * percent_change
        else:
            self.price -= self.price * percent_change

    def print_info(self):
        print(self.name, self.price, self.category)