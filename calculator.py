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

def try_again():
    # clear the input fields
    entry_1.delete(0, END)
    entry_2.delete(0, END)
    # clear the result label
    result_label.config(text="")

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
        

        # design UI
        # import tkinter, messagebox
        from tkinter import *
        from tkinter import messagebox
        # create display for user input
        root = Tk()
        root.title("Calculator")
        root.config(bd=15)

        # create the try again button
        try_again_button = Button(root, text="Try Again", command=try_again)
        try_again_button.grid(row=4, column=0)

        # drop down operation selection design
        operation_ui = Label(root, text="Select an operation (+, -, *, /): ")
        operation_ui.grid(row=0, column=0)
        operation_var = StringVar(root)
        operation_var.set("+")
        operation_dropdown = OptionMenu(root, operation_var, "+", "-", "*", "/")
        operation_dropdown.grid(row=0, column=1)

        num_1 = Label(root, text = "Enter the first number: ")
        num_1.grid(row = 2, column = 0)
        entry_1 = Entry(root)
        entry_1.grid(row = 2, column = 1)

        num_2 = Label(root, text = "Enter the second number: ")
        num_2.grid(row = 3, column = 0)
        entry_2 = Entry(root)
        entry_2.grid(row = 3, column = 1)

        def solve():
                messagebox.showinfo("RESULT", "World")

        button = Button(root, text = "Solve", command = solve)
        button.grid(row = 4, column = 1)

        # create button to perform arithmetic operation and display result
        button = Button(root, text="Solve", command=solve)
        button.grid(row=3, column=1)
        # ask if the user wants to try again
        try_again = input("Do you want to try again? (yes or no): ")
        if try_again.lower() != "yes":
            # user doesn't want to try again, exit the loop
            break

root.mainloop()
sys.exit()
# button for result 
# show result
