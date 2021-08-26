from Administrator import Administrator
from Customer import Customer
from DataBase import DataBase
from Department import Department
from User import User


# доробити
class SessionManager:
    db = DataBase()

    def __init__(self):
        pass

    def add_user(self, user_id: str, password: str, name: str, role: str, email: str = "", address: str = "",
                 phone: int = 0, credit_card_info: str = "", shipping_info: str = ""):
        if role == "admin":
            return Administrator(user_id, password, name, email)
        elif role == "customer":
            return Customer(user_id, password, name, address, email, phone, credit_card_info, shipping_info)

    def get_user(self, user_id: str) -> User:
        SessionManager.db.cursor.execute("SELECT * FROM Users WHERE userId =(?) ", (user_id,))
        user = SessionManager.db.cursor.fetchone()
        if user is None:
            return None
        user_id = user[0]
        password = user[1]
        name = user[2]
        email = user[3]
        role = user[4]
        address = user[5]
        phone = user[6]
        credit_card_info = user[7]
        shipping_info = user[8]
        if role == "admin":
            return Administrator(user_id, password, "unknown", name, email)
        elif role == "customer":
            return Customer(user_id, password, name, address, email, phone, credit_card_info, shipping_info)

    def get_department(self, dep_name: str) -> Department:
        # Пошук департеманта
        SessionManager.db.cursor.execute("SELECT * FROM Department WHERE departmentName =(?) ", (dep_name,))
        dep = SessionManager.db.cursor.fetchone()
        department_description = dep[0]
        department_id = dep[1]
        department_name = dep[2]

        return Department(department_id, department_name, department_description)
