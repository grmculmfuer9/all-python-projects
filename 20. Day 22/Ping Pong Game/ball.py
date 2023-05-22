from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.07

    def move(self):
        """Move the ball in appropriate direction"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_with_y(self):
        """Changes the y direction of the ball"""
        self.y_move *= -1

    def bounce_with_x(self):
        """Changes the x direction of the ball"""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """Reset the position"""
        self.goto(x=0, y=0)
        self.move_speed = 0.08
