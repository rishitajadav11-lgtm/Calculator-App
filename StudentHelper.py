import math

def odd_even_checker():
    num = int(input("Enter a number to check if it is Odd or Even: "))
    if num % 2 == 0:
        print(f"{num} is Even.")
    else:
        print(f"{num} is Odd.")

def scientific_calculator():
    print("\n--- Scientific Calculator ---")
    print("1. Square Root")
    print("2. Power")
    print("3. Logarithm")
    print("4. Sine")
    print("5. Cosine")
    print("6. Tangent")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        num = float(input("Enter number: "))
        print(f"√{num} = {math.sqrt(num)}")
    elif choice == 2:
        base = float(input("Enter base: "))
        exponent = float(input("Enter exponent: "))
        print(f"{base}^{exponent} = {math.pow(base, exponent)}")
    elif choice == 3:
        num = float(input("Enter number: "))
        print(f"log({num}) = {math.log(num)}")
    elif choice == 4:
        angle = float(input("Enter angle in degrees: "))
        print(f"sin({angle}) = {math.sin(math.radians(angle))}")
    elif choice == 5:
        angle = float(input("Enter angle in degrees: "))
        print(f"cos({angle}) = {math.cos(math.radians(angle))}")
    elif choice == 6:
        angle = float(input("Enter angle in degrees: "))
        print(f"tan({angle}) = {math.tan(math.radians(angle))}")
    else:
        print("Invalid choice in scientific calculator.")

def math_calculator():
    print("\n--- Mathematical Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter your choice (1-4): "))

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        print(f"{num1} + {num2} = {num1 + num2}")
    elif choice == 2:
        print(f"{num1} - {num2} = {num1 - num2}")
    elif choice == 3:
        print(f"{num1} * {num2} = {num1 * num2}")
    elif choice == 4:
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Division by zero is not allowed.")
    else:
        print("Invalid choice in mathematical calculator.")

def result_calculator():
    n = int(input("Enter Your Total Subject's :- "))
    total =0 

    for i in range(1, n+1):
        mark = float(input(f"Enter Your Marks of Subject {i} :-"))
        total += mark

    percentage = total / n

    print("Your Total Marks of All Subjects:- ", total)
    print("Your Percentage of All Subjects :- ", percentage, "%")

def main_menu():
    while True:
        print("\n========== Calculator Menu ==========")
        print("1. Odd/Even Checker")
        print("2. Scientific Calculator")
        print("3. Mathematical Calculator")
        print("4. Result Calculator")
        print("5. Exit")
        print("=====================================")

        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            odd_even_checker()
        elif choice == 2:
            scientific_calculator()
        elif choice == 3:
            math_calculator()
        elif choice == 4:
            result_calculator()
        elif choice == 5:
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid menu choice. Please choose between 1 and 5.")

if __name__ == "__main__":
    main_menu()
