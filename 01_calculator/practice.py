import math

print("Welcome to CyberCalculator！")
print("-" * 40)

while True:
    print("\nPlease select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("0. Exit")

    operation = input("Enter your choice: ")

    if operation == "0":
        print("Goodbye!")
        break

    elif operation == "1":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 + num2
        print("Result:", result)

    elif operation == "2":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 - num2
        print("Result:", result)

    elif operation == "3":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 * num2
        print("Result:", result)

    elif operation == "4":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 != 0:
            result = num1 / num2
            print("Result:", result)
        else:
            print("Error: Division by zero")

    elif operation == "5":
        num = float(input("Enter a number: "))
        if num >= 0:
            result = math.sqrt(num)
            print("Result:", result)
        else:
            print("Error: Cannot calculate square root of a negative number")

    else:
        print("Invalid choice, please try again.")
