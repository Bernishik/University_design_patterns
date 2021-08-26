from abc import ABCMeta
from quack_behavior import QuackBehavior
from fly_behavior import FlyBehavior


class Duck(metaclass=ABCMeta):
    fly_behavior: FlyBehavior
    quack_behavior: QuackBehavior

    def display(self):
        pass

    def perform_fly(self):
        self.fly_behavior.fly()

    def swim(self):
        print("All ducks float, even decoys!")

    def perform_quack(self):
        self.quack_behavior.quack()

    def set_fly_behavior(self, fb: FlyBehavior):
        self.fly_behavior = fb

    def set_quack_behavior(self, qb: QuackBehavior):
        self.quack_behavior = qb
