def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"
def main():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    while True:
        choice = input("Enter choice (1/2/3/4): ")
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue
            if choice == '1':
                result = add(num1, num2)
                print(f"The result of {num1} + {num2} is {result}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"The result of {num1} - {num2} is {result}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"The result of {num1} * {num2} is {result}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"The result of {num1} / {num2} is {result}")
            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                break
        else:
            print("Invalid choice. Please select a valid operation.")
if __name__ == "__main__":
    main()