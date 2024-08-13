def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculate(n1, n2, func):
    return func(n1, n2)


result = calculate(4, 4, add)
print(f"\tresult:{result}")
