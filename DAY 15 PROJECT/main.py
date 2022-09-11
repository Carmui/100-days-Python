import data

is_ended = True
profit = 0

def enough_resources(ingrediendts):
    """Ingredient checker """
    for item in ingrediendts:
        if ingrediendts[item] >= data.resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def coin_calculate():
    """Calculate coins for the payment"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_rec, drink_cost):
    """Return True when the payment is accepted, False if not enough money"""
    if money_rec >= drink_cost:
        change = round(money_rec - drink_cost, 2)
        print(f"Here is your change: {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, not enough money. Money refunded.")
        return False

def make_coffe(drink_name, order_ing):
    for item in order_ing:
        data.resources[item] -= order_ing[item]
    print(f"Here is your {drink_name}")

while is_ended:
    choice = input("What would you like (espresso/latte/cappuccino):")
    if choice == "off":
        is_ended = False
    elif choice == "report":
        print(f"Water: 100ml: {data.resources['water']} ml")
        print(f"Milk: 50ml: {data.resources['milk']} ml")
        print(f"Coffee: 76g: {data.resources['coffee']} g")
        print(f"Money: ${profit}")
    else:
        drink = data.MENU[choice]
        print(drink)
        if enough_resources(drink["ingredients"]):
            payment = coin_calculate()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffe(choice, drink["ingredients"])