from tkinter import *

def button_click(digit):
    current = result.get()
    result.delete(0, END)
    result.insert(0, str(current) + str(digit))
    
def clear_btn():
    result.delete(0, END)
    
def add_digits():
    first_number = result.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    result.delete(0, END)
    
def equal_func():
    second_number = result.get()
    result.delete(0, END)
    
    if math == "addition":
        result.insert(0, f_num + int(second_number))
        
    if math == "subtraction":
        result.insert(0, f_num - int(second_number))
        
    if math == "multiplication":
        result.insert(0, f_num * int(second_number))
        
    if math == "division":
        result.insert(0, f_num / int(second_number))
    
def subtract_btn():
    first_number = result.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    result.delete(0, END)

def multiply_btn():
    first_number = result.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    result.delete(0, END)

def divide_btn():
    first_number = result.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    result.delete(0, END)

root = Tk()
root.title("Calculator")
root.resizable(0, 0)

result = Entry(root, width=35, borderwidth=5)
result.grid(column=0, row=0, columnspan=5, pady=10, padx=10)


# Defining Buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=39, pady=20, command=add_digits)
button_equal = Button(root, text="=", padx=91, pady=20, command=equal_func)
button_clear = Button(root, text="C", padx=91, pady=20, command=clear_btn)


button_subtract = Button(root, text="-", padx=41, pady=20, command=subtract_btn)
button_multiply = Button(root, text="*", padx=40, pady=20, command=multiply_btn)
button_divide = Button(root, text="/", padx=40, pady=20, command=divide_btn)



# Display Buttons
button_1.grid(row=3, column=0,)
button_2.grid(row=3, column=1,)
button_3.grid(row=3, column=2,)

button_4.grid(row=2, column=0,)
button_5.grid(row=2, column=1,)
button_6.grid(row=2, column=2,)


button_7.grid(row=1, column=0,)
button_8.grid(row=1, column=1,)
button_9.grid(row=1, column=2,)


button_0.grid(row=4, column=0,)
button_clear.grid(row=4,columnspan=2, column=1)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0,)
button_multiply.grid(row=6, column=1,)
button_divide.grid(row=6, column=2,)


root.mainloop()