from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position

    def create_paddle(self):
        """Make a paddle and place it at the given position"""
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.left(90)
        self.goto(self.position)

    def go_up(self):
        """Moves the paddle upwards"""
        if self.distance(370, 280) > 50 and self.distance(-370, 280) > 50:
            self.forward(20)

    def go_down(self):
        """Moves the paddle downwards"""
        if self.distance(370, -280) > 50 and self.distance(-370, -280) > 50:
            self.backward(20)
