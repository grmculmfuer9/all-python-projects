# Coffee Machine
from resources import resources, menu
"""Espresso: 50ml water, 18g coffee, 1.50$
Latte: 200ml water, 24g coffee, 150ml milk, 2.50$
250ml water, 24g coffee, 100ml milk, 3.50$
Penny: 1 cent
Nickel: 5 cents
Dime: 10 cents
Quarter: 25 cents
TODO: 1. Report tells resources we have
TODO: 2. Check resources are sufficient
TODO: 3. Process Coins
TODO: 4. Checking transaction successful
TODO: 5. Make coffee"""
is_game_over = False
water_left = resources["water"]
milk_left = resources["milk"]
coffee_left = resources["coffee"]
profit = 0


def is_sufficient(order_ingredients):
    """Tells if the ingredients required to make the coffee are enough"""
    for i in order_ingredients['ingredients']:
        # print(i)
        if order_ingredients['ingredients'][i] > resources[i]:
            print(f"Sorry there is not enough {i}.")
            return False
    return True


def process_coins():
    """Ask how much money the user have and return the total"""
    print("Please insert coins.")
    quarters = int(input("How many quarter: ")) * 0.25
    dimes = int(input("How many dimes: ")) * 0.10
    nickels = int(input("How many nickels: ")) * 0.05
    pennies = int(input("How many pennies: ")) * 0.01
    return quarters + dimes + nickels + pennies


def is_transaction(final_user_amount, amount_required):
    """Confirm if the user have enough money"""
    return final_user_amount >= amount_required


def make_coffee(coffee_type):
    """Deduct the resources used to make the coffee and make the coffee"""
    for i in resources:
        resources[i] -= menu[coffee_type]['ingredients'][i]
    print(f"Here is your {coffee_type} ☕️. Enjoy!")


while not is_game_over:
    type_of_coffee = input("What would you like? (espresso/latte/cappuccino): ")
    if type_of_coffee == "off" or type_of_coffee == "end" or type_of_coffee == "no":
        is_game_over = True
    elif type_of_coffee == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: ${profit}")
    else:
        order = menu[type_of_coffee]
        # print(menu, order)
        if is_sufficient(order):
            total = process_coins()
            amount = menu[type_of_coffee]['cost']
            if is_transaction(total, amount):
                profit += amount
                print(f"Here is ${float(total - amount)} in change.")
                make_coffee(type_of_coffee)
            else:
                print("Sorry that's not enough money. Money refunded.")
