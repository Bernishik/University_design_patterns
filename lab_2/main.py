from Container import Container
from Ball import Ball

ball = Ball(50, 50, 5, 10, 30)
box = Container(0, 0, 100, 100)
for step in range(0, 100):
   ball.move()
   box.collides(ball)
   print(ball)   # check the position of the ball


