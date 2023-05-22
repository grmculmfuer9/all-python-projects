import turtle
FONT = ("Arial", 10, "normal")


class PlaceTheCoordinates(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def place_the_answer(self, coordinates, answer):
        """Place the given answer on given coordinates"""
        self.goto(coordinates)
        self.write(arg=answer, align="center", font=FONT)
