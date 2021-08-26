import random
import string

from DataBase import DataBase


class ShippingInfo:
    db = DataBase()

    def __init__(self, shipping_type: str, shipping_cost: int, shipping_region_id: int,
                 shipping_id: int = int(''.join(random.choices(string.digits, k=8)))):
        self._shipping_id = shipping_id
        self._shipping_type = shipping_type
        self._shipping_cost = shipping_cost
        self._shipping_region_id = shipping_region_id

    def update_shipping_info(self, shipping_type: str, shipping_cost: int, shipping_region_id: int):
        self._shipping_type = shipping_type
        self._shipping_cost = shipping_cost
        self._shipping_region_id = shipping_region_id

    @property
    def shipping_id(self):
        return self._shipping_id

    def create(self) -> bool:
        ShippingInfo.db.cursor.execute("SELECT count(*) FROM ShippingInfo WHERE shippingId = (?)",
                                       (int(self._shipping_id),))
        check_unicue_id = ShippingInfo.db.cursor.fetchone()[0]
        if check_unicue_id > 0:
            # raise Exception("Id is already taken")
            print("Id is already taken")
            return False

        ShippingInfo.db.cursor.execute(
            "INSERT INTO ShippingInfo(shippingId,shippingType,shippingCost,shippingRegionId) VALUES (?,?,?,?)",
            (int(self._shipping_id), str(self._shipping_type), int(self._shipping_cost), int(self._shipping_region_id)))
        ShippingInfo.db.connection.commit()
        return True

    @staticmethod
    def get_shipping_info(shipping_id: int):
        ShippingInfo.db.cursor.execute("SELECT * FROM ShippingInfo WHERE shippingId = (?)", (shipping_id,))
        data = ShippingInfo.db.cursor.fetchone()
        if data is None:
            return data
        shipping_id = data[0]
        shipping_type = data[1]
        shipping_cost = data[2]
        shipping_region_id = data[3]
        return ShippingInfo(shipping_type,shipping_cost,shipping_region_id,shipping_id)
