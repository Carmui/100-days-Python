from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_ended = True
profit = 0

coffee_maker = CoffeeMaker()
machine = MoneyMachine()
menu = Menu()

machine.report()
coffee_maker.report()


while is_ended:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_ended = False
    elif choice == "report":
        machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)