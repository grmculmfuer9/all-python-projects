from prettytable import PrettyTable


# All User Details
class AllUserDetails:
    def __init__(self):
        self.name = None
        self.age = None
        self.gender = None
        self.amount = None

        self.all_user_details = PrettyTable()
        self.all_user_details.field_names = ["Name", "Age", "Gender"]

        self.all_user_account_details = PrettyTable()
        self.all_user_account_details.field_names = ["Name", "Age", "Gender", "Amount"]

    def add_user_details(self, banking_current_user):
        self.name = banking_current_user.name
        self.age = banking_current_user.age
        self.gender = banking_current_user.gender
        self.all_user_details.add_row([self.name, self.age, self.gender])

    def add_account_details(self, banking_current_user):
        self.name = banking_current_user.name
        self.age = banking_current_user.age
        self.gender = banking_current_user.gender
        self.amount = banking_current_user.balance
        self.all_user_account_details.add_row([self.name, self.age, self.gender, self.amount])

    def show_user_details(self):
        print(self.all_user_details)

    def show_user_account_details(self):
        print(self.all_user_account_details)
