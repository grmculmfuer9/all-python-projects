from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_item = MenuItem
menu = Menu()
is_game_over = False
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while not is_game_over:
    menu_item.name = input(f"What would you like? {menu.get_items()}: ")
    if menu_item.name == "off" or menu_item.name == "no" or menu_item.name == "end":
        is_game_over = True
    elif menu_item.name == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        details_drink = menu.find_drink(menu_item.name)
        if details_drink != None:
            are_resources_sufficient = coffee_maker.is_resource_sufficient(details_drink)
            if are_resources_sufficient:
                 # money = input("How much money will you pay: $")
                 is_money_enough = money_machine.make_payment(details_drink.cost)
                 if is_money_enough:
                     coffee_maker.make_coffee(details_drink)
        else:
            # print("Invalid Item! Please try again!")
            pass
