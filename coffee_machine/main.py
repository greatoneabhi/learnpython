from art import logo

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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def is_resource_sufficient(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def insert_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    dollars = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    return dollars


is_machine_running = True
while is_machine_running:
    print(logo)
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if "report" == choice:
        print(
            f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${profit}"
        )
    elif "off" == choice:
        is_machine_running = False
    else:
        if is_resource_sufficient(MENU[choice]["ingredients"]):
            amount_paid = insert_coins()
            if amount_paid < MENU[choice]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                change = "{:.2f}".format(amount_paid - MENU[choice]["cost"])
                print(f"Here is ${change} dollars in change.")
                print(f"Here is your {choice} ☕. Enjoy!")
                profit += MENU[choice]["cost"]
                resources["water"] = (
                    resources["water"] - MENU[choice]["ingredients"]["water"]
                )

                if "espresso" != choice:
                    resources["milk"] = (
                        resources["milk"] - MENU[choice]["ingredients"]["milk"]
                    )

                resources["coffee"] = (
                    resources["coffee"] - MENU[choice]["ingredients"]["coffee"]
                )
