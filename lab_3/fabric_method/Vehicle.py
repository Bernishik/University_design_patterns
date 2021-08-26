from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def info(self):
        pass


class Bike(Vehicle):
    def __init__(self):
        self.info()

    def info(self):
        print("its a bike")


class Car(Vehicle):
    def __init__(self):
        self.info()

    def info(self):
        print("its a Car")


class Truck(Vehicle):
    def __init__(self):
        self.info()

    def info(self):
        print("its a Truck")


class Crane(Vehicle):
    def __init__(self):
        self.info()

    def info(self):
        print("its a Crane")
