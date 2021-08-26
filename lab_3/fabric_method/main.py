from VehicleStore import *

light_factory = LightVehicleStore()
heavy_factory = HeavyVehicleStore()

bike1 = light_factory.create_vehicle("Bike")
bike2 = light_factory.create_vehicle("Bike")
car = light_factory.create_vehicle("Car")
truck1 = heavy_factory.create_vehicle("Truck")
crane = heavy_factory.create_vehicle("Crane")
truck2 = heavy_factory.create_vehicle("Truck")

print(light_factory.get_order_list())
print(heavy_factory.get_order_list())



