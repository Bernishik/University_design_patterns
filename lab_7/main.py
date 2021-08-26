from mallard_duck import MallardDuck
from model_duck import ModelDuck
from fly_rocket_powered import FlyRocketPowered


mallard = MallardDuck()
mallard.perform_fly()
mallard.perform_quack()

model = ModelDuck()
model.perform_fly()
model.set_fly_behavior(FlyRocketPowered())
model.perform_fly()
