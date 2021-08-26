import random
import string

from Category import Category
from DataBase import DataBase


# готовий
class Department:
    db = DataBase()

    def __init__(self, name: str, description: str,
                 department_id: str = str(''.join(random.choices(string.digits, k=8)))):
        self._description = description
        self._name = name
        # я би хотів забрати department_id на користь primary key в бд, але нехай буде
        self._department_id = department_id

    @property
    def name(self):
        return self._name

    def get_category_in_department(self) -> list:
        # пошук категорій в департеманті
        Category.db.cursor.execute("SELECT * FROM Category WHERE departmentName = (?)"
                                   , (self._name,))
        data = Category.db.cursor.fetchall()

        category_list = []
        if data.__len__() > 0:
            for cat in data:
                category_id = cat[0]
                department_name = cat[1]
                category_name = cat[2]
                description = cat[3]
                category_list.append(Category(department_name, category_name, description, category_id, ))
        return category_list

    def add_department(self) -> bool:
        Department.db.cursor.execute("SELECT count(*) FROM Department WHERE departmentId = (?) OR departmentName = (?)", (self._department_id,self._name))
        check_unique_id = Department.db.cursor.fetchone()[0]
        if check_unique_id > 0:
            # raise Exception("Id or Name is already taken")
            print("Cannot add department: Id or Name is already taken")
            return False
        Department.db.cursor.execute("INSERT INTO Department(departmentId,departmentName,description) VALUES (?,?,?)",
                                     (str(self._department_id), str(self._name), str(self._description)))
        Department.db.connection.commit()
        return True

    def delete_department(self):
        Department.db.cursor.execute("DELETE FROM Department WHERE departmentName = (?)", (int(self._name),))
        Department.db.cursor.execute("UPDATE Category SET departmentName = (?) WHERE departmentName = (?)",
                                     (0, int(self._name)))
        Department.db.connection.commit()

    @staticmethod
    def get_department_by_name(department_name: str):
        Department.db.cursor.execute("SELECT * FROM Department WHERE departmentName = (?)", (str(department_name),))
        data = Department.db.cursor.fetchone()
        if data is None:
            return None
        department_id = data[0]
        department_name = data[1]
        description = data[2]
        return Department(department_name, description, department_id)

    @staticmethod
    def get_department(department_id: int):
        Department.db.cursor.execute("SELECT * FROM Department WHERE departmentId = (?)", (int(department_id),))
        data = Department.db.cursor.fetchone()
        if data is None:
            return None
        department_id = data[0]
        department_name = data[1]
        description = data[2]
        return Department(department_name, description, department_id)

    @staticmethod
    def get_all_departments() -> list:
        Department.db.cursor.execute("SELECT * FROM Department ")
        data = Department.db.cursor.fetchall()
        departments_list = []
        if data.__len__() > 0:
            for dep in data:
                department_id = dep[0]
                department_name = dep[1]
                description = dep[2]
                departments_list.append(Department(department_name, description, department_id))
        return departments_list
