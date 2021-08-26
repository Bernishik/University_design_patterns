import numpy


class Ball:
    def __init__(self, x: float, y: float, radius: int, speed: int, direction: int):
        self._x = x
        self._y = y
        self._radius = radius
        self._speed = speed
        self._direction = direction
        self._x_delta = self._speed * numpy.cos(numpy.radians(self._direction))
        self._y_delta = -self._speed * numpy.sin(numpy.radians(self._direction))

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value: float):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @property
    def x_delta(self):
        return self._x_delta

    @x_delta.setter
    def x_delta(self, value):
        self._x_delta = value

    @property
    def y_delta(self):
        return self._y_delta

    @y_delta.setter
    def y_delta(self, value):
        self._y_delta = value

    def move(self):
        self._x += self._x_delta
        self._y += self._y_delta

    def reflect_horizontal(self):
        self._x_delta = -self._x_delta

    def reflect_vertical(self):
        self._y_delta = -self._y_delta

    def __str__(self):
        return "Ball at(" + str(round(self.x, 2)) + "," + str(round(self.y, 2)) + ") of velocity (" + \
               str(round(self.x_delta, 2)) + "," + str(
            round(self.y_delta, 2)) + ")"
