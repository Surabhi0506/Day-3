#WAP to create a calculator that has a menu system where it asks for a choice from the user (+,-,*,/,!(factorial)). It should display the output until the user explicitly terminates the program by writing exit
while True:
    print("\n... Calculator Menu ....")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Factorial (!)")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", num1 + num2)

    elif choice == "2":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", num1 - num2)

    elif choice == "3":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", num1 * num2)

    elif choice == "4":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            print("Result:", num1 / num2)

    elif choice == "5":
        n = int(input("Enter a positive integer: "))
        if n < 0:
            print("Factorial does not exist for negative numbers.")
        else:
            fact = 1
            for i in range(1, n + 1):
                fact = fact * i
            print("Result:", fact)

    elif choice == "6":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice, please select between 1 and 6.")