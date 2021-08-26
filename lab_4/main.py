import random
import string

from Administrator import Administrator
from Category import Category
from Customer import Customer
from Department import Department
from Product import Product
from Orders import Orders
import datetime

from SessionManager import SessionManager
from ShoppingCart import ShoppingCart

sesManag = SessionManager()
user = sesManag.add_user("qwerty", "pass", "name", "customer", "as", "asa", 1231, "asdas", "asdas")
admin = sesManag.add_user("qwertyAdmin", "pass", "name", "admin", "Asda")

user.register()
admin.register()
prod1 = Product("prod1", "prod1", 14, "as", 12431)
prod2 = Product("prod2", "prod1", 14, "as", 12412)
prod3 = Product("prod3", "prod1", 14, "as", 12413)

prod1.add_product()
prod2.add_product()
prod3.add_product()

shopping = ShoppingCart()
shopping.add_cart_item(prod1, 1)
shopping.add_cart_item(prod2, 2)
shopping.add_cart_item(prod3, 3)

shopping.view_cart_details()
user.take_order(shopping, "post", 12, 14)
user_order = Orders.get_orders_by_user_id("qwerty").pop()
print(user_order._order_id)
prod4 = Product("prod4", "prod1", 14, "as")
prod4.add_product("keker")
admin.create_category("keker", "asfdasdfa", "dep1")
admin.create_department("dep1", "asdasfas")
admin.create_category("keker", "asfdasdfa", "dep1")
prod4.add_product("keker")

dep12 = sesManag.get_department("dep1")
user12 = sesManag.get_user("qwerty")

print(user12.user_id)
print(dep12.name)

Product.get_product(12431).delete_product()
Product.get_product(12412).delete_product()
Product.get_product(12413).delete_product()
