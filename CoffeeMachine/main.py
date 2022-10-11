money = 0
water = 300
milk = 200
coffee = 100
run = True
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: 1. Print the report of all coffee machine


def report():
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")


def coin_calculator():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    money_gave = 0.25*quarters + 0.10*dimes + 0.05*nickles + 0.01*pennies
    return money_gave


# TODO: 2. Check resources sufficient to make drink order


def requirement(w_need, c_need, m_need):
    if w_need > water:
        print("Sorry their is not enough water")
        return 1
    if c_need > coffee:
        print("Sorry their is not enough coffee")
        return 1
    if m_need > milk:
        print("Sorry their is not enough milk")
        return 1
    return 0


def espresso():
    cont = requirement(50, 18, 0)
    global money, water, coffee
    if cont == 0:
        print("Please insert coins.")
        input_money = coin_calculator()
        change = round(input_money - 1.50, 2)
        if change > 0:
            money += 1.50
            coffee -= 18
            water -= 50
            print(f"Here is ${change} in change")
            print("Here is your espresso ☕ Enjoy!")
        elif change < 0:
            print("Sorry that's not enough money. Money refunded")


def latte():
    cont = requirement(200, 24, 150)
    global money, water, milk, coffee
    if cont == 0:
        print("Please insert coins.")
        input_money = coin_calculator()
        change = round(input_money - 2.50, 2)
        if change > 0:
            money += 2.50
            coffee -= 24
            water -= 200
            milk -= 150
            print(f"Here is ${change} in change")
            print("Here is your latte ☕ Enjoy!")
        elif change < 0:
            print("Sorry that's not enough money. Money refunded")


def cappuccino():
    cont = requirement(250, 24, 100)
    global money, water, milk, coffee
    if cont == 0:
        print("Please insert coins.")
        input_money = coin_calculator()
        change = round(input_money - 3.00, 2)
        if change > 0:
            money += 3.00
            coffee -= 24
            water -= 250
            milk -= 100
            print(f"Here is ${change} in change")
            print("Here is your cappuccino ☕ Enjoy!")
        elif change < 0:
            print("Sorry that's not enough money. Money refunded")


def coffee_machine():
    global run
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee_type == 'espresso':
        espresso()
    elif coffee_type == 'latte':
        latte()
    elif coffee_type == 'cappuccino':
        cappuccino()
    elif coffee_type == 'report':
        report()
    elif coffee_type == 'off':
        run = False


while run:
    coffee_machine()
