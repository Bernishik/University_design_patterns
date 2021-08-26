import datetime
import random
import string

from DataBase import DataBase
from OrderDetail import OrderDetail
from ShippingInfo import ShippingInfo


# CUSTOMARE NAME
class Orders:
    db = DataBase()

    def __init__(self, customer_id: str, status: str = "created",
                 date_created: str = datetime.datetime.now(), date_shipped: str = "",
                 shipping_id: int = None,
                 order_id: int = int(''.join(random.choices(string.digits, k=8)))
                 ):
        self._order_id = order_id
        self._date_created = date_created
        self._date_shiped = date_shipped
        self._shipping_id = shipping_id
        self._status = status
        self._customer_id = customer_id
        self._order_list = []

    def place_order(self):
        if self._order_list.__len__() > 0 and self._shipping_id is not None:
            # відправка ордера в бд
            self._date_created = datetime.datetime.now()
            Orders.db.cursor.execute("SELECT count(*) FROM Orders WHERE orderId = (?)",
                                     (int(self._order_id),))
            check_unique_id = Orders.db.cursor.fetchone()[0]
            if check_unique_id > 0:
                # raise Exception("Id is already taken")
                print("Id is already taken")
                return False

            Orders.db.cursor.execute(
                "INSERT INTO Orders(orderId,dateCreated,dateShipped,customerId,status,shippingId)"
                " VALUES (?,?,?,?,?,?)", (int(self._order_id), str(self._date_created), str(self._date_shiped),
                                          str(self._customer_id), str(self._status), str(self._shipping_id)))
            Orders.db.connection.commit()
            for detail in self._order_list:
                detail.create()
            self._shipping_info.create()
            return True
        else:
            # raise Exception("order list or shipping info is not defined")
            print("Cannot place order: order list or shipping info is not defined")
            return False

    def add_order_detail(self, product_id: int, quantity: int):
        self._order_list.append(OrderDetail(self._order_id, product_id, quantity))


    def set_shipping_info(self, type, cost, redion_id, ):
        self._shipping_info = ShippingInfo(type, cost, redion_id)
        self._shipping_id = self._shipping_info.shipping_id

    def set_shipping_info_by_id(self, shipping_id):
        self._shipping_info = ShippingInfo.get_shipping_info(shipping_id)
        self._shipping_id = self._shipping_info.shipping_id

    @staticmethod
    def get_order(order_id: int):
        Orders.db.cursor.execute("SELECT * FROM ORDERS WHERE orderId = (?)", (order_id,))
        data = Orders.db.cursor.fetchone()
        if data is None:
            return None
        order_id = data[0]
        date_created = data[1]
        date_shipped = data[2]
        customer_id = data[3]
        status = data[4]
        shipping_id = data[5]
        return Orders(customer_id, status, date_created, date_shipped, shipping_id, order_id)

    @staticmethod
    def get_orders_by_user_id(user_id):
        Orders.db.cursor.execute("SELECT * FROM ORDERS WHERE customerId = (?)", (user_id,))
        data = Orders.db.cursor.fetchall()
        orders = []
        if data.__len__() > 0:
            for order in data:
                order_id = order[0]
                date_created = order[1]
                date_shipped = order[2]
                customer_id = order[3]
                status = order[4]
                shipping_id = order[5]
                orders.append(Orders(customer_id, status, date_created, date_shipped, shipping_id, order_id))
        return orders
