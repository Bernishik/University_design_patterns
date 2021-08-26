class GearBoxType:

    def __init__(self, name: str, remarks: str):
        self.name = name
        self.remarks = remarks


class GearBox:

    def __init__(self, gearRatio: float, currentGear: int, type: GearBoxType):
        self.gearRatio = gearRatio
        self.currentGear = currentGear
        self.type = type

    def shiftUp(self):
        pass

    def shiftDown(self):
        pass


class Tire:

    def __init__(self, width: float, airPressure: float):
        self.width = width
        self.airPressure = airPressure


class Wheel:

    def __init__(self, diameter: float, tire: Tire):
        self.diameter = diameter
        self.tire = tire


class Suspention:
    def __init__(self, springRate: float, wheel: Wheel):
        self.springRate = springRate
        self.wheel = wheel


class Brake:
    def __init__(self, type: str, wheel: Wheel):
        self.type = type
        self.wheel = wheel

    def apply(self):
        pass


class CarModel:
    def __init__(self, title: str):
        self.title = title


class Engine:

    def __init__(self, capacity: float, numberOfCylinders: int):
        self.capacity = capacity
        self.numberOfCylinders = numberOfCylinders

    def start(self):
        pass

    def brake(self):
        pass

    def accerate(self):
        pass


class Body:
    def __init__(self, numberOfDoors: int):
        self.numberOfDoors = numberOfDoors


class Car:

    def __init__(self, registrationNum: str, year: int, licenseNum: str, gearBox: GearBox, suspension: Suspention,
                 brake: Brake, body: Body, engine: Engine):
        self.registrationNum = registrationNum
        self.year = year
        self.license_num = licenseNum
        self.gear_box = gearBox
        self.suspension = suspension
        self.brake = brake
        self.body = body
        self.engine = engine

    def moveForward(self):
        pass

    def moveBackward(self):
        pass

    def stop(self):
        pass

    def tumRight(self):
        pass

    def tumLeft(self):
        pass


gear_box_type = GearBoxType("name", "remarks")
gear_box = GearBox(2.2,2,gear_box_type)
tire = Tire(2,2.4)
wheel = Wheel(4,tire)
suspension = Suspention(3,wheel)
brake = Brake("type",wheel)
body = Body(4)
engine = Engine(5,5)
car_model = CarModel("model")
myCar = Car("num",21,"num",gear_box,suspension,brake,body,engine)

# переробити, всі поля зробити нормальними
