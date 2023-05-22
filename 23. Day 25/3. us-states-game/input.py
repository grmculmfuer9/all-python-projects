import turtle

TOTAL_CORRECT_ANSWERS = 50


class Input:
    def __init__(self):
        self.correct_answers = 0
        self.screen = turtle.Screen()

    def popup(self, score):
        """Ask user for the answer"""
        user_state = self.screen.textinput(title=f"{score}/50 states correct", prompt="What's another "
                                                                                      "state's name?").title()
        return user_state
