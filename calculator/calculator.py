def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculate(symbol, a, b):
    if symbol not in OPERATIONS:
        raise ValueError(f"Unknown operation: {symbol}")
    return OPERATIONS[symbol](a, b)


if __name__ == "__main__":
    expressions = [("+", 2, 3), ("-", 7, 4), ("*", 6, 5), ("/", 8, 2)]
    for symbol, a, b in expressions:
        print(a, symbol, b, "=", calculate(symbol, a, b))
