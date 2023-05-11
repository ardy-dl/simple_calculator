# import exit module
import sys
# create method
def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

repeat = True
while repeat:
# ask the user for operation
    operation = input("Select an operation (+, -, *, /): ")
# ask for two numbers
    try:
        num_1 = float(input("Enter the first number: "))
        num_2 = float(input("Enter the second number: "))
    except ValueError:
        print("Sorry! Only numbers are accepted.")
    # display result
    else:
        if operation == "+":
            print(num_1, "+", num_2, "=", addition(num_1,num_2))
        elif operation == "-":
            print(num_1, "-", num_2, "=", subtraction(num_1,num_2))
        elif operation == "*":
            print(num_1, "*", num_2, "=", multiplication(num_1,num_2))
        elif operation == "/":
            if num_2 == 0:
                print("Cannot divide by zero.")
            else:
                print(num_1, "/", num_2, "=", division(num_1,num_2))
        else:
            print("Invalid operation")
# ask if want to try again
    try_again = input("Do you want to try again? (yes or no): ")
    if try_again.lower() != "yes":
        repeat = False
        print("Thank you for using the calculator")
        sys.exit()
# design UI