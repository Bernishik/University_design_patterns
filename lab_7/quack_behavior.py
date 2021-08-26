from abc import ABCMeta, abstractmethod


class QuackBehavior(metaclass=ABCMeta):
    @abstractmethod
    def quack(self):
        pass
