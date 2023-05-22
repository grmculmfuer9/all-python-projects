from user import User
from prettytable import PrettyTable


# Child Class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        # self.convert_details_into_prettytable()

        self.account_details = PrettyTable()
        self.account_details.field_names = ["Deposit", "Withdraw Amount", "Balance"]

        self.balance = 0

    def convert_details_into_prettytable_amount(self, mode, amount, complete):
        if mode == "deposit":
            self.account_details.add_row(row=[f"${amount}", None, f"${self.balance}"])
        elif mode == "withdraw":
            if complete:
                self.account_details.add_row(row=[None, f"${amount}", f"${self.balance}"])
            else:
                self.account_details.add_row(row=[None, f"NP: ${amount}", f"${self.balance}"])

    def deposit(self, amount):
        self.balance += amount
        self.convert_details_into_prettytable_amount(mode="deposit", amount=amount, complete=False)
        print(f"Account balance has been updated: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            self.convert_details_into_prettytable_amount(mode="withdraw", amount=amount, complete=False)
            print(f"Insufficient Balance | Account Balance: ${self.balance}")
        else:
            self.balance -= amount
            self.convert_details_into_prettytable_amount(mode="withdraw", amount=amount, complete=True)
            print(f"Account balance has been updated: ${self.balance}")

    def view_balance_history(self):
        self.show_details()
        print()
        print(f"Account Balance:\n{self.account_details}")
