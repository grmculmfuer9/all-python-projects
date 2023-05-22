import pandas


class ReadAllStates:
    def __init__(self):
        self.all_states = None
        self.states = []
        self.missing_states = []
        self.read_the_states()

    def read_the_states(self):
        """Read the states, make their list, and read the file"""
        self.all_states = pandas.read_csv("50_states.csv")
        self.states = self.all_states.state.to_list()

    def confirm_the_answer(self, user_answer):
        """Confirm if the answer was correct"""
        if user_answer in self.all_states.state.to_list():
            result = self.all_states[self.all_states.state == user_answer]["x"].to_list()
            result.extend(self.all_states[self.all_states.state == user_answer]["y"].to_list())
            return tuple(result)
        return False

    def store_missing_states(self, guessed_states):
        """Return the states that were not named during the game"""
        self.missing_states = [x for x in self.states if x not in guessed_states]

        df = pandas.DataFrame(self.missing_states)
        df.to_csv("missing_states.csv")
