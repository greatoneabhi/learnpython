from calculator_art import logo
import os


def display_logo():
    print(logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def pick_operation():
    print("+\n-\n*\n/")
    return input("Pick an operation: ")


def perform_operation(n1, operation, n2):
    if operation == "+":
        return add(n1, n2)
    elif operation == "-":
        return subtract(n1, n2)
    elif operation == "*":
        return multiply(n1, n2)
    elif operation == "/":
        return divide(n1, n2)
    else:
        print("Unsupported operation!")


def calculator(operations):
    result = 0
    first_number = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        # operation = pick_operation()
        operation = input("Pick an operation: ")
        next_number = float(input("What's the next number?: "))
        # result = perform_operation(
        #    n1=first_number, operation=operation, n2=next_number
        # )
        calculate = operations[operation]
        result = calculate(n1=first_number, n2=next_number)
        print(f"{first_number} {operation} {next_number} = {result}")
        choice = input(
            f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: "
        ).lower()
        if choice == "y":
            first_number = result
        elif choice == "n":
            os.system("clear")
            calculator(operations)
        else:
            print("Wrong choice! Exiting...")
            should_continue = False


def main():
    display_logo()
    operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
    calculator(operations)


if __name__ == "__main__":
    main()
