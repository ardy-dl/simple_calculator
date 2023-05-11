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
        

# design UI
# import tkinter, messagebox
from tkinter import *
from tkinter import messagebox
# create display for user input
root = Tk()
root.title("Calculator")
root.config(bd=15)
# drop down operation selection design
operation_ui = Label(root, text="Select an operation (+, -, *, /): ")
operation_ui.grid(row=0, column=0)
operation_var = StringVar(root)
operation_var.set("+")
operation_dropdown = OptionMenu(root, operation_var, "+", "-", "*", "/")
operation_dropdown.grid(row=0, column=1)

num_1 = Label(root, text = "Enter the first number: ")
num_1.grid(row = 2, column = 0)
entry_2 = Entry(root)
entry_2.grid(row = 2, column = 1)

num_2 = Label(root, text = "Enter the second number: ")
num_2.grid(row = 3, column = 0)
entry_3 = Entry(root)
entry_3.grid(row = 3, column = 1)

def solve():
        messagebox.showinfo("RESULT", "World")

button = Button(root, text = "Solve", command = solve)
button.grid(row = 4, column = 1)

root.mainloop()
sys.exit()
# button for result 
# show result
