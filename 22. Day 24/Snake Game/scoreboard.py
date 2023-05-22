from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(x=0, y=250)
        self.hideturtle()

        with open(file="data.txt") as file:
            self.high_score = int(file.read())

        self.score = 0
        self.write_score()

    def increment(self):
        """Increment the score"""
        self.score += 1
        self.write_score()

    def write_score(self):
        """Increment and write the score on top of the screen"""
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score

            with open(file="data.txt", mode="w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.write_score()
