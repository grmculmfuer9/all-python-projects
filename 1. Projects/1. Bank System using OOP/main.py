# Bank System using OOP
"""
todo: Parent Class: User
        1. Holds details about a user (Complete)
        2. Has a function to show user details (Complete)
todo: Child Class: Bank
        1. Stores details about the account balance
        2. Stores details about the amount
        3. Allows for deposits, withdraw, and view_balance
"""
from bank import Bank
from all_users_details import AllUserDetails
from logo import logo

every_user_details = AllUserDetails()
banking_current_user = None

name = age = gender = ""
amount = 0
exit_the_program = False

print("Welcome to Banking App")
print(logo)
while not exit_the_program:
    print()
    print(f"Choose a choice:")
    print("1. View details of all the users")
    print("2. View details of all the users with their final balance")
    print("3. Add new user")
    print("4. Deposit balance to the current user")
    print("5. Withdraw balance from the current user")
    print("6. View details of the current user")
    print("7. View balance history of the current user")
    print("8. Exit")
    user_choice = int(input("What is your choice, enter the number: "))

    if user_choice == 1:
        if banking_current_user is None:
            print("No user exits right now")
        else:
            every_user_details.show_user_details()
    elif user_choice == 2:
        if banking_current_user is None:
            print("No user exits right now")
        else:
            every_user_details.show_user_account_details()
    elif user_choice == 3:
        if banking_current_user is not None:
            every_user_details.add_account_details(banking_current_user=banking_current_user)
        name = input("What is the name of the new user: ")
        age = int(input("What is the age of the new user: "))
        gender = input("What is the gender of the new user: ")
        banking_current_user = Bank(name=name, age=age, gender=gender)
        banking_current_user.convert_details_into_prettytable()
        every_user_details.add_user_details(banking_current_user=banking_current_user)
    elif user_choice == 4:
        if banking_current_user is None:
            print("No user exists right now.")
            continue
        amount = int(input("How much amount you want to deposit: $"))
        banking_current_user.deposit(amount=amount)
    elif user_choice == 5:
        if banking_current_user is None:
            print("No user exists right now.")
            continue
        amount = int(input("How much amount you want to withdraw: $"))
        banking_current_user.withdraw(amount=amount)
    elif user_choice == 6:
        if banking_current_user is None:
            print("No user exists right now")
        else:
            banking_current_user.show_details()
    elif user_choice == 7:
        if banking_current_user is None:
            print("No user exists right now")
        else:
            banking_current_user.view_balance_history()
    elif user_choice == 8:
        exit_the_program = True
    else:
        print("Wrong choice, please try again!")
