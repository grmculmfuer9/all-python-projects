from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Write the given score"""
        self.clear()
        self.goto(-100, 200)
        self.write(arg=self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(arg=self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        """Increases the point for left hand player"""
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """Increases the point for right hand player"""
        self.r_score += 1
        self.update_scoreboard()

    def write_the_winner(self, winner_name):
        """Output the winner of the game using the given name as a parameter"""
        self.goto(0, 0)
        self.write(arg=f"{winner_name} WON!", align="center", font=("Courier", 30, "normal"))
