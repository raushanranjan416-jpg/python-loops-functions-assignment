operations = ["+", "-", "*", "/", "%", "exit"]


def get_number(message: str):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Error: Please enter a valid number")


def calculate(first_number: float, second_number: float, operation: str):
    if operation == "+":
        return first_number + second_number
    elif operation == "-":
        return first_number - second_number
    elif operation == "*":
        return first_number * second_number
    elif operation == "/":
        return first_number / second_number
    elif operation == "%":
        return first_number % second_number


while True:
    print("=== Calculator  ===")
    operation = input("Please choose operation between: + , -, * , / , %, exit ")

    if operation == "exit":
        print("=== exit  ===")
        break

    if operation not in operations:
        print("Please choose valid operation between: + , -, * , / , %, exit")
        continue

    first_number = get_number("Enter your first number ")
    second_number = get_number("Enter your second number ")

    while operation in ["/", "%"] and second_number == 0:
        print("Divide by zero is not possible")
        second_number = get_number("Enter your second number again ")

    print(f"{first_number} {operation} {second_number} : ", calculate(first_number, second_number, operation))
