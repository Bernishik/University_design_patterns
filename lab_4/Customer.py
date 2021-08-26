from Administrator import Administrator
from DataBase import DataBase
from Orders import Orders
from Product import Product
from ShoppingCart import ShoppingCart
from User import User


class Customer(User):
    db = DataBase()

    def __init__(self, user_id: str, password: str, customer_name: str, address: str, email: str,
                 phoneno: int, credit_card_info: str, shipping_info: str, login_status: str = "offline", ):

        super().__init__(user_id, password, login_status, role="customer")
        self._shipping_info = shipping_info
        self._credit_card_info = credit_card_info
        self._email = email
        self._address = address
        self._name = customer_name
        self._phoneno = phoneno
        # self._shopping_cart = []
        self._product_list = []

    def verify_login(self) -> bool:
        # перевірка на вхід
        Customer.db.cursor.execute("SELECT * FROM Users WHERE userId =(?) ", (self._user_id,))
        check_user = Customer.db.cursor.fetchone()
        if check_user is None:
            print("No such user")
            return False
        password = check_user[1]
        if self._password == password:
            return True
        else:
            return False

    def register(self) -> bool:
        Customer.db.cursor.execute("SELECT count(*) FROM Users WHERE userId =(?) ", (self._user_id,))
        check_unicue_id = Customer.db.cursor.fetchone()[0]
        if check_unicue_id == 0:
            Customer.db.cursor.execute(
                "INSERT INTO Users(userId,password,name,email,role,address,phone,creditCardInfo,ShippingInfo)"
                "VALUES (?,?,?,?,?,?,?,?,?)", (self._user_id, self._password, self._name,
                                               self._email, self._role, self._address,
                                               self._phoneno, self._credit_card_info, self._shipping_info))
            Customer.db.connection.commit()
            return True
        return False

    def login(self):
        if self.verify_login():
            print("you are logged")
            self._login_status = "online"

    def update_profile(self):
        if self.verify_login():
            Customer.db.cursor.execute("UPDATE Users SET password = (?),name =(?),email = (?),address = (?),"
                                       " phone = (?),creditCardInfo = (?), ShippingInfo = (?) WHERE userId = (?)",
                                       (self._password, self._name,
                                        self._email, self._role, self._address,
                                        self._phoneno, self._credit_card_info, self._shipping_info, self._user_id,))
            Customer.db.connection.commit()
            return True
        return False

    @staticmethod
    def search(product_id: int):
        Customer.db.cursor.execute("SELECT * FROM Products WHERE productId =(?) ", (product_id,))
        prod = Customer.db.cursor.fetchone()
        if prod is None:
            return False
        product_id = prod[0]
        product_name = prod[1]
        product_description = prod[2]
        product_price = prod[3]
        product_image_file_name = prod[4]
        return Product(product_name, product_description, product_price, product_image_file_name, product_id)

    @property
    def name(self):
        return self._name

    def take_order(self, shopping_cart: ShoppingCart, shipping_type,cost:int,region_id:int):
        product_list = shopping_cart.checkout()
        if product_list.__len__() > 0:
            order = Orders(self._user_id)
            for item in product_list:
                data = ShoppingCart.get_item_details(item)
                product_id = data[0]
                quantity = data[3]
                order.add_order_detail(product_id, quantity)
            order.set_shipping_info(shipping_type, cost, region_id)
            order.place_order()
        else:
            print("product list is empty")
