class Store():
    def __init__(self, store_name):
        self.store_name = store_name
        self.products = []

    def add_products(self, product):
        # if product not in self.available_prodcuts:
        self.products.append(product)

    

Giant = Store("Giant")


class Product():
    def __init__(self, name, price, category, available_at):
        self.name = name
        self.price = price
        self.category = category
        self.available_at = available_at
        self.available_at.add_products(self)

    def __str__(self):
        return f"{self.name}"

toilet_paper = Product('Charmin Toilet Paper', '19.99','household', Giant)

for p in Giant.products:
    print(p)