from duck import Duck
from quack import Quack
from fly_no_way import FlyNoWay


class ModelDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Quack()

    def display(self):
        print("Модель качки")
