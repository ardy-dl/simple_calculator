# import exit module
# design UI
# import tkinter, messagebox
from tkinter import *
from tkinter import messagebox

# create methods
def addition(num_1, num_2):
    return num_1 + num_2

def subtraction(num_1, num_2):
    return num_1 - num_2

def multiplication(num_1, num_2):
    return num_1 * num_2

def division(num_1, num_2):
    return num_1 / num_2

def try_again():
    # clear the input fields
    entry_1.delete(0, END)
    entry_2.delete(0, END)
    # clear the result label
    
repeat = True
while repeat:
    def solve():
        try:  
            num_1 = float(entry_1.get())
            num_2 = float(entry_2.get())
            operation = operation_var.get()

        except ValueError:
            messagebox.showerror("Error:", "Sorry! Only numbers are accepted.")

        if operation == "+":
            result = addition(num_1, num_2)
            messagebox.showinfo("Result", f"{num_1} + {num_2} = {result}")       
        elif operation == "-":
            result = subtraction(num_1, num_2)
            messagebox.showinfo("Result", f"{num_1} - {num_2} = {result}")
        elif operation == "*":
            result = multiplication(num_1, num_2)
            messagebox.showinfo("Result", f"{num_1} * {num_2} = {result}")
        elif operation == "/":
                if num_2 == 0:
                    messagebox.showerror("Error:","Cannot divide by zero.")
                else:
                    result = division(num_1, num_2)
                    messagebox.showinfo("Result", f"{num_1} / {num_2} = {result}")

    # display result
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

    num_1_ui = Label(root, text = "Enter the first number: ")
    num_1_ui.grid(row = 2, column = 0)
    entry_1 = Entry(root)
    entry_1.grid(row = 2, column = 1)

    num_2_ui = Label(root, text = "Enter the second number: ")
    num_2_ui.grid(row = 3, column = 0)
    entry_2 = Entry(root)
    entry_2.grid(row = 3, column = 1)

    # create button to perform arithmetic operation and display result
    button = Button(root, text="Solve", command = solve)
    button.grid(row = 4, column = 1)

    try_again = input("Do you want to try again? (yes or no): ")
    if try_again.lower() != "yes":
		    # user doesn't want to try again, exit the loop
        break
root.mainloop()
# button for result 
# show result
