
from threading import local
from unicodedata import name
import math


class Store():
    def __init__(self, store_name):
        self.store_name = store_name
        self.available_prodcuts = []

    def add_products(self, product):
        # if product not in self.available_prodcuts:
        self.available_prodcuts.append(product)
        return self

    def show_product_info(self):
        print (f'{self.store_name}')
        for product in self.available_prodcuts:
            product.print_info()

    def sell_product(self, id):
        if id in self.available_prodcuts:
            self.available_prodcuts.remove(id)
            return (f'{id} has been sold')

    def inflation(self, x):
        for product in self.available_prodcuts:
            product.price += (product.price * x )/ 100
            return self
            

class Product():
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        # self.available_at = available_at
        # self.available_at.add_products(self.name, self.price)

    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price += (self.price * percent_change) / 100
        else:
            self.price -= math.ceil(self.price * percent_change) / 100
        return (f'{self.price}')

    def print_info(self):
        print (f'{self.name}, {self.price}, {self.category}')

Giant = Store("Giant")
Sams = Store("Sams")
BestBuy = Store("Best Buy")

local_stores = [Giant, Sams, BestBuy ]

toilet_paper = Product('charmin', 19.99,'household')
blender = Product('Ninja', 149.99,'household')
tv = Product('Sony', 1999.99,'household')

factory = [toilet_paper, blender, tv]

BestBuy.add_products(tv)
Giant.add_products(toilet_paper).add_products(blender)
Sams.add_products(toilet_paper).add_products(blender).add_products(tv)

# for x in local_stores:
#     x.show_product_info()

# for x in factory:
#     print(x.print_info())

for x in local_stores:
    x.inflation(1.8).show_product_info()

for x in factory:
    print(x.update_price(1.8, True))

# for x in local_stores:
#     print(x.sell_product('Sony'))

BestBuy.sell_product('Sony')

for x in local_stores:
    x.show_product_info()