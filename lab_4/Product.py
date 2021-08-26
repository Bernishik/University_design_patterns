# готовий
import random
import sqlite3
import string

from DataBase import DataBase


class Product:
    db = DataBase()

    def __init__(self, name: str, description: str, price: int, image_file_name: str,
                 product_id: int = int(''.join(random.choices(string.digits, k=8)))):
        self._image_file_name = image_file_name
        self._price = price
        self._description = description
        self._name = name
        self._product_id = product_id

    def display_product(self):
        return self._image_file_name

    def get_product_details(self) -> str:
        return "Product name: " + self._name + " id: " + str(
            self._product_id) + " description: " + self._description \
               + " price:" + str(self._price)

    @staticmethod
    def get_product(product_id: int):

        Product.db.cursor.execute('SELECT * FROM Products WHERE productId = (?)', (int(product_id),))
        data = Product.db.cursor.fetchone()
        if data is None:
            return None
        product_id = int(data[0])
        name = str(data[1])
        description = str(data[2])
        price = int(data[3])
        image_file_name = str(data[4])
        return Product(name, description, price, image_file_name, product_id)

    @staticmethod
    def get_products_by_name(product_name: str):

        Product.db.cursor.execute('SELECT * FROM Products WHERE productName = (?)', (product_name,))
        data = Product.db.cursor.fetchall()
        product_list = []
        if data.__len__() > 0:
            for prod in data:
                product_id = int(prod[0])
                name = prod[1]
                description = prod[2]
                price = int(prod[3])
                image_file_name = prod[4]
                product_list.append(Product(name, description, price, image_file_name, product_id))
        return product_list

    def add_product(self, category_name: str = "NoCategory") -> bool:

        Product.db.cursor.execute("SELECT count(*) FROM Products WHERE productId = (?)",
                                  (self._product_id,))
        check_unique_id = Product.db.cursor.fetchone()[0]
        Product.db.cursor.execute("SELECT count(*) FROM Category WHERE categoryName = (?)",
                                  (category_name,))
        check_category = Product.db.cursor.fetchone()[0]
        if check_unique_id > 0:
            # raise Exception("Id is already taken")
            print("Cannot add product: Id is already taken")
            return False

        if check_category == 0:
            # raise Exception("Id is already taken")
            print("Cannot add product: No such category with name: " + category_name)
            return False

        Product.db.cursor.execute(
            'INSERT INTO Products(productId,productName,description,price,imageFileName,categoryName) VALUES (?,?,?,?,?,?)',
            (self._product_id, self._name, self._description, self._price,
             self._image_file_name,
             category_name))
        Product.db.connection.commit()

        return True

    def delete_product(self) -> bool:
        success = True
        try:
            Product.db.cursor.execute('DELETE FROM Products WHERE productId = (?)', (self._product_id,))
            Product.db.connection.commit()
        except sqlite3.Error:
            success = False
        return success




    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def product_id(self):
        return self._product_id
