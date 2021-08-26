import random
import string

from DataBase import DataBase
from Product import Product


# готовий
class Category:
    db = DataBase()

    def __init__(self, department_name: str, category_name: str, description: str,
                 category_id: int = int(''.join(random.choices(string.digits, k=8)))):
        self._description = description
        self._category_name = category_name
        self._department_name = department_name
        self._category_id = category_id

    def add_category(self) -> bool:

        Category.db.cursor.execute("SELECT count(*) FROM Category WHERE categoryName = (?)", (self._category_name,))
        check_unique_id = Category.db.cursor.fetchone()[0]
        Category.db.cursor.execute("SELECT count(*) FROM Department WHERE departmentName = (?)", (self._department_name,))
        check_dep = Category.db.cursor.fetchone()[0]
        if check_unique_id > 0:
            # raise Exception("Id is already taken")
            print("Cannot add Category: name is already taken")
            return False

        if check_dep == 0:
            # raise Exception("Id is already taken")
            print("Cannot add Category: No such department with name: " + self._department_name)
            return False

        Category.db.cursor.execute(
            "INSERT INTO Category(categoryId,departmentName,categoryName,description) VALUES (?,?,?,?)",
            (self._category_id, self._department_name, self._category_name, self._description))
        Category.db.connection.commit()
        return True

    def delete_category(self):

        Category.db.cursor.execute("DELETE  FROM Category WHERE categoryId = (?)", (int(self._category_id),))
        Category.db.cursor.execute("UPDATE Products SET categoryName = (?) WHERE categoryName = (?)",
                                   (0, self._category_name))
        Category.db.connection.commit()

    @staticmethod
    def get_category_by_name(category_name: str):

        Category.db.cursor.execute("SELECT * FROM Category WHERE categoryName = (?)", (str(category_name),))
        data = Category.db.cursor.fetchone()
        if data is None:
            print("No such category")
            return None
        category_id = data[0]
        department_name = data[1]
        category_name = data[2]
        description = data[3]
        return Category(department_name, category_name, description, category_id)

    @staticmethod
    def get_category(category_id: int):

        Category.db.cursor.execute("SELECT * FROM Category WHERE categoryId = (?)", (int(category_id),))
        data = Category.db.cursor.fetchone()
        if data is None:
            return None
        category_id = data[0]
        department_name = data[1]
        category_name = data[2]
        description = data[3]
        return Category(department_name, category_name, description, category_id)

    @staticmethod
    def get_all_category() -> list:

        Category.db.cursor.execute("SELECT * FROM Category ")
        data = Category.db.cursor.fetchall()
        category_list = []
        if data.__len__() > 0:
            for cat in data:
                department_name = cat[0]
                category_name = cat[1]
                description = cat[2]
                category_id = cat[3]
                category_list.append(Category(department_name, category_name, description, category_id))
        return category_list

    def get_products_in_category(self) -> list:

        Category.db.cursor.execute("SELECT * FROM Products WHERE categoryId = (?)", (int(self._category_id),))
        data = Category.db.cursor.fetchall()
        product_list = []
        if data.__len__() > 0:
            for prod in data:
                name = prod[0]
                description = prod[1]
                price = prod[2]
                image_file_name = str(prod[3])
                product_id = prod[4]
                product_list.append(Product(name, description, price, image_file_name, product_id))
        return product_list
