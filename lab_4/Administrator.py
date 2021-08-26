from Category import Category
from DataBase import DataBase
from Department import Department
from Product import Product
from User import User


class Administrator(User):
    db = DataBase()

    def __init__(self, user_id: str, password: str, admin_name: str,
                 email: str, login_status: str = "offline"):
        super().__init__(user_id, password, login_status,"admin")
        self._email = email
        self._name = admin_name

    def verify_login(self):
        # перевірка на вхід
        Administrator.db.cursor.execute("SELECT * FROM Users WHERE userId =(?) ", (self._user_id,))
        check_user = Administrator.db.cursor.fetchone()
        if check_user is None:
            print("No such user")
            return False
        password = check_user[1]
        if self._password == password:
            return True
        else:
            return False

    def register(self) -> bool:
        Administrator.db.cursor.execute("SELECT count(*) FROM Users WHERE userId =(?) ", (self._user_id,))
        check_unicue_id = Administrator.db.cursor.fetchone()[0]
        if check_unicue_id == 0:
            Administrator.db.cursor.execute(
                "INSERT INTO Users(userId,password,name,email,role)"
                "VALUES (?,?,?,?,?)", (self._user_id, self._password, self._name,
                                       self._email, self._role,))
            Administrator.db.connection.commit()
            return True
        return False

    def login(self):
        if self.verify_login():
            print("you are logged")
            self._login_status = "online"

    def create_department(self, department_name: str, description: str) -> None:
        dep = Department(department_name, description)
        dep.add_department()

    def create_category(self, category_name: str, description: str, department_name: str):
        cat = Category(department_name, category_name, description)
        cat.add_category()

    def create_product(self, product_name: str, description: str, price: int, image_file_name: str,
                       category_name: str = "NoCategory"):
        prod = Product(product_name, description, price, image_file_name)
        prod.add_product(category_name)

    def delete_department(self, department_name: str):
        Department.get_department_by_name(department_name).delete_department()

    def delete_category(self, category_name: str):
        Category.get_category_by_name(category_name).delete_category()

    def delete_product(self, product_id: int):
        Product.get_product(product_id).delete_product()

    def edit_catalog_details(self):
        pass
