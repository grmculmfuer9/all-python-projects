from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Remake another food on the screen at random"""
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        self.goto(x, y)
