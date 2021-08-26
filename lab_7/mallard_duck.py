from duck import Duck
from quack import Quack
from fly_with_wrings import FlyWithWrings


class MallardDuck(Duck):
    def __init__(self):
        self.quack_behavior = Quack()
        self.fly_behavior = FlyWithWrings()

    def display(self):
        print("Я справжня mallard качка")
