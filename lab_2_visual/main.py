from Ball import Ball
from Container import Container
from Window import Window

box = Container(0, 0, 500, 500)
width = box.x2
height = box.y2
centre_x, centre_y = width / 2, height / 2
ball = Ball(centre_x, centre_y, 50, 5, 120)
window = Window(ball, box)
