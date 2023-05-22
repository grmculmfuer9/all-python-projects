from prettytable import PrettyTable


# Parent Class
class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.user = PrettyTable()

    def convert_details_into_prettytable(self):
        self.user.field_names = ["Name", "Age", "Gender"]
        self.user.add_row(row=[self.name, self.age, self.gender])

    def show_details(self):
        print("Personal Details: ")
        print()
        print(self.user)
