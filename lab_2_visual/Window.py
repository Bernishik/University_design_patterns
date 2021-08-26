import time
from tkinter import *
from Container import Container
from Ball import Ball


class Window:
    def __init__(self, ball: Ball, box: Container):
        self.window = Tk()
        self.window.resizable(False, False)
        self.window.title("ball")
        self.box = box
        self.width = box.x2
        self.height = box.y2

        self.ball = ball
        self.radius = self.ball.radius
        self.canvas = Canvas(self.window, width=self.width, height=self.height, bg="#002")
        self.circle = self.canvas.create_oval([self.ball.x - self.radius, self.ball.y - self.radius],
                                              [self.ball.x + self.radius, self.ball.y + self.radius],
                                              fill='green')
        self.canvas.pack()
        self.play = True
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.circle_animate()

        self.window.mainloop()

    def circle_animate(self):
        while self.play:
            self.ball.move()
            self.box.collides(self.ball)
            print(self.ball)
            self.canvas.coords(self.circle, self.ball.x - self.radius, self.ball.y - self.radius,
                               self.ball.x + self.radius, self.ball.y + self.radius)
            self.window.update()
            time.sleep(0.005)

    def on_closing(self):
        self.canvas.destroy()
        self.window.destroy()
        self.play = False
