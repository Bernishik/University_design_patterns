from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, user_id: str, password: str, login_status: str,role:str):
        self._user_id = user_id
        self._password = password
        self._login_status = login_status
        self._role = role
    @abstractmethod
    def verify_login(self):
        pass

    @property
    def user_id(self):
        return self._user_id