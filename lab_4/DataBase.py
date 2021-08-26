import os
import sqlite3


# готовий
class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class DataBase(metaclass=MetaSingleton):
    connection = None
    abs_path = os.getcwd()
    DB_path = os.path.join(abs_path, "DB")
    db_path = os.path.join(DB_path, "database.db")

    def __init__(self):
        if self.connection is None:
            if not os.path.exists(self.DB_path):
                os.makedirs('DB')
            self.connection = sqlite3.connect(self.db_path)
            self.cursor = self.connection.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS Users(userId CHARACTER UNIQUE , password VARCHAR, name CHARACTER ,"
                            "email VARCHAR, role CHARACTER,address VARCHAR , phone INTEGER, creditCardInfo VARCHAR,ShippingInfo VARCHAR)")
        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS Products(productId INTEGER UNIQUE ,productName CHARACTER,'
            'description VARCHAR , price INTEGER , imageFileName VARCHAR , categoryName CHARACTER )')

        category_name = "NoCategory"
        category_description = "NoCategory"
        department_name = "NoDepartment"
        department_description = "NoDepartment"
        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS Category(categoryId INTEGER UNIQUE  ,departmentName CHARACTER ,'
            'categoryName CHARACTER UNIQUE ,description VARCHAR )')
        self.cursor.execute(
            'INSERT OR IGNORE  INTO Category(categoryId,departmentName, categoryName,description) VALUES (?,?,?,?)',
            (0, department_name, category_name, category_description))


        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS Department('
            'departmentId INTEGER UNIQUE ,departmentName CHARACTER UNIQUE , description VARCHAR )')
        self.cursor.execute(
            'INSERT OR IGNORE  INTO Department(departmentId , departmentName,description) VALUES (?,?,?)',
            (0, department_name, department_description))

        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS Orders(orderId INTEGER UNIQUE,dateCreated VARCHAR,dateShipped VARCHAR,'
            'customerId CHARACTER,status CHARACTER,shippingId INTEGER)')
        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS OrdersDetail(orderId INTEGER ,productId INTEGER,quantity INTEGER)')
        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS ShippingInfo(shippingId INTEGER UNIQUE ,shippingType VARCHAR,'
            'shippingCost INTEGER,shippingRegionId INTEGER)')
        self.connection.commit()
