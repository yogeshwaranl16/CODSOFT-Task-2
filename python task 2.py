def add(x, y):

    return x + y

def subtract(x, y):

    return x - y

def multiply(x, y):

    return x * y

def divide(x, y):

    if y == 0:

        return "Error! Division by zero."

    else:

        return round(x / y, 2)

print("Select Calculation:")

print("A. Add")

print("B. Subtract")

print("C. Multiply")

print("d. Divide")

while True:

    choice = input("Enter choice (A/B/C/D): ")

    if choice in ('A','B', 'C', 'D'):

        try:

            num1 = float(input("Enter first number: "))

            num2 = float(input("Enter second number: "))

        except ValueError:

            print("Invalid input. Please enter valid numbers.....")

            continue

        if choice == 'A':

            print("Result:", add(num1, num2))

        elif choice == 'B':

            print("Result:", subtract(num1, num2))

        elif choice == 'C':

           print("Result:", multiply(num1, num2))

        elif choice == 'D':

           print("Result:", divide(num1, num2))

    else:

        print("Invalid input. Please enter a valid choice (A/B/C/D).")
