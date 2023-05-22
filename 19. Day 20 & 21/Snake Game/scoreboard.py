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
        self.score = 0
        self.write_score()

    def increment(self):
        """Increment the score"""
        self.score += 1

    def write_score(self):
        """Increment and write the score on top of the screen"""
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        """Inform the user when the game is over"""
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
