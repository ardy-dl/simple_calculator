# create method
def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

# ask the user for operation
operation = input("Select an operation (+, -, *, /): ")

# ask for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
# process the inputs
if operation == "+":
    print(num1, "+", num2, "=", addition(num1,num2))
elif operation == "-":
    print(num1, "-", num2, "=", subtraction(num1,num2))
elif operation == "*":
    print(num1, "+", num2, "=", addition(num1,num2))
elif operation == "/":
    print(num1, "+", num2, "=", addition(num1,num2))
else:
    print("Invalid operation")
# display result
# ask if want to try again
# if yes, repeat from step 1
# else, print "thank you" and exit the program
# design UI

