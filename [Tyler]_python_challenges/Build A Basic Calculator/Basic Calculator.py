def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

def get_user_input() -> tuple[float, float]:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    return a, b

def display_menu() -> str:
    print("\nCalculator Menu:")
    print("1. Add ")
    print("2. Subtract ")
    print("3. Multiply ")
    print("4. Divide ")
    print("5. Exit ")
    return input("Choose an operation (1-5): ")

def main() -> None:
    while True:
        choice = display_menu()
        if choice == '5':
            print("Goodbye! ")
            break

        try:
            num1, num2 = get_user_input()

            if choice == '1':
                result = add(num1, num2)
                print(f"Result: {num1} + {num2} = {result}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"Result: {num1} - {num2} = {result}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"Result: {num1} * {num2} = {result}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"Result: {num1} / {num2} = {result}")
            else:
                print("Invalid choice. Please select from 1 to 5.")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()

