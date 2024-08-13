from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
cofee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        cofee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink is not None:
            if cofee_maker.is_resource_sufficient(drink) and money_machine.make_payment(
                drink.cost
            ):
                cofee_maker.make_coffee(drink)
