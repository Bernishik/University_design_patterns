from Ball import Ball


class Container:
    def __init__(self, x: int, y: int, width: int, height: int):
        self._x = x
        self._y = y
        self._x2 = x + width
        self._y2 = x + height

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def x2(self):
        return self._x2

    @property
    def y2(self):
        return self._y2

    def collides(self, ball: Ball):
        x1 = ball.x - ball.radius
        x2 = ball.x + ball.radius
        y1 = ball.y - ball.radius
        y2 = ball.y + ball.radius
        if x1 <= self.x or x2 >= self.x2:
            ball.reflect_horizontal()
        if y1 <= self.y or y2 >= self.y2:
            ball.reflect_vertical()

    def __str__(self):
        return "Container at (" + str(self.x) + "," + str(self.y) + ") to (" + str(self.x2) + "," + str(self.y2) + ")"
