import random
import string

from CartItem import CartItem
from Product import Product


class ShoppingCart:
    def __init__(self, cart_id: int = int(''.join(random.choices(string.digits, k=8)))):
        self._cart_id = cart_id
        self._cart_list = []

    def add_cart_item(self, product: Product, quantiry):
        self._cart_list.append(CartItem(self._cart_id, product, quantiry))

    def delete_cart_item(self,product_id:int):
        for item in self._cart_list:
            if item.product_id == product_id:
                self._cart_list.pop(self._cart_list.index(item))
                return True
        return False


    def update_quantity(self,product_id:int,quantity:int):
        for item in self._cart_list:
            if item.product_id == product_id:
                item.quantity(quantity)
                return True
        return False

    def view_cart_details(self):
        print("Products in cart:")
        for item in self._cart_list:
            print("Product Id: " + str(item.product_id) + " Product name: " + str(item.name) + " price: " + str(item.unit_cost)
                  + " quantity: " + str(item.quantity) + " subtotal: " + str(item.subtotal))

    @staticmethod
    def get_item_details(item) ->list:
        detail = []
        detail.append(item.product_id)
        detail.append(item.name)
        detail.append(item.unit_cost)
        detail.append(item.quantity)
        detail.append(item.subtotal)
        return detail

    def checkout(self):
        # оформлення ордера
        return self._cart_list

    def calc_total_price(self):
        total = 0
        for item in self._cart_list:
            total += item.subtotal
        return total
