from abc import ABCMeta, abstractmethod


class FlyBehavior(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass
