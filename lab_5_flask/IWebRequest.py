from abc import ABC, abstractmethod


class IWebRequest(ABC):
    @abstractmethod
    def request(self, obj) -> bool:
        pass
