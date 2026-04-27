def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

def multiply(a, b):
    return a * b


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("[!] Please enter a valid number.")


def calculator():
    while True:
        user_input = input("""
>>>>>>>> Please select an operation <<<<<<<<
1. Addition
2. Subtraction
3. Division
4. Multiplication
Press E to exit
Choice: """).lower()

        if user_input == 'e':
            print("Calculator exited.")
            break

        if user_input not in {'1', '2', '3', '4'}:
            print("[!] Invalid choice. Try again.\n")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if user_input == '1':
            result = add(num1, num2)
        elif user_input == '2':
            result = subtract(num1, num2)
        elif user_input == '3':
            result = divide(num1, num2)
        elif user_input == '4':
            result = multiply(num1, num2)

        print(f"\nResult: {result}\n")


if __name__ == "__main__":
    calculator()