from DataBase import DataBase
from Product import Product


class OrderDetail:
    db = DataBase()

    def __init__(self, order_id: int, product_id: int, quantity: int):
        self._order_id = order_id
        self._product_id = product_id
        self._product = Product.get_product(self._product_id)
        self._product_name = self._product.name
        self._unit_cost = self._product.price
        self._quantity = quantity
        self._subtotal = self.calc_price()

    def calc_price(self) -> float:
        return self._unit_cost * self._quantity

    def create(self):

        OrderDetail.db.cursor.execute(
            "INSERT INTO OrdersDetail(orderId  ,productId  ,quantity) VALUES (?,?,?)",
            (self._order_id, self._product_id, self._quantity))
        OrderDetail.db.connection.commit()
