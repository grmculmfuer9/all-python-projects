from turtle import Turtle


class Walls(Turtle):
    def __init__(self):
        super().__init__()
        pass

    def make_wall(self):
        """Make a wall"""
        self.penup()
        self.hideturtle()
        self.goto(290, 290)
        self.color("white")
        self.width(10)

        self.pendown()

        for i in range(4):
            self.draw()

    def draw(self):
        """Draw the side of the wall"""
        self.right(90)
        self.forward(580)
