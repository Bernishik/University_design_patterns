from Product import Product


class CartItem:
    def __init__(self, cart_id: int, product: Product, quantity: int):

        self._cart_id = cart_id
        self._quantity = quantity
        self._unit_cost = product.price
        self._name = product.name
        self._product_id = product.product_id
        self._subtotal = self.calc_price()

    def calc_price(self):
        return self._unit_cost * self._quantity

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self,value):
        self._quantity = value

    @property
    def unit_cost(self):
        return self._unit_cost

    @property
    def name(self):
        return self._name

    @property
    def product_id(self):
        return self._product_id

    @property
    def subtotal(self):
        return self._subtotal

